//! Remote model manifest (plan step 1): verified GGUF URLs, sizes,
//! quants, and RAM requirements, updatable over-the-air. Falls back to a
//! bundled copy and then to any stale cache, so the app works offline.

use std::path::Path;

use serde::{Deserialize, Serialize};

use crate::{downloader, scanner::MemInfo};

/// One downloadable model entry.
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct ManifestEntry {
    pub id: String,
    pub url: String,
    pub params_b: f64,
    pub quant: String,
    pub min_ram_kb: u64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Manifest {
    pub models: Vec<ManifestEntry>,
}

impl Manifest {
    pub fn from_json(text: &str) -> Result<Self, String> {
        serde_json::from_str(text).map_err(|e| e.to_string())
    }

    /// Built-in copy used when offline with no cache.
    pub fn bundled() -> Self {
        Self::from_json(include_str!("../assets/default-manifest.json"))
            .expect("bundled manifest is valid")
    }

    pub fn find(&self, id: &str) -> Option<&ManifestEntry> {
        self.models.iter().find(|m| m.id == id)
    }
}

/// Fetch the manifest from `url`, caching it at `cache`. On any failure,
/// return the stale cache, else the bundled copy. Never errors.
pub async fn load(url: &str, cache: &Path) -> Manifest {
    if downloader::download(url, cache, false, |_| {}).await.is_ok() {
        if let Ok(text) = tokio::fs::read_to_string(cache).await {
            if let Ok(m) = Manifest::from_json(&text) {
                return m;
            }
        }
    }
    if let Ok(text) = tokio::fs::read_to_string(cache).await {
        if let Ok(m) = Manifest::from_json(&text) {
            return m;
        }
    }
    Manifest::bundled()
}

/// Compatibility of one manifest entry with scanned hardware.
#[derive(Debug, PartialEq, Eq)]
pub enum Badge {
    RunsFast,
    TightFit,
    ExceedsRam,
}

pub fn badge(entry: &ManifestEntry, mem: &MemInfo) -> Badge {
    if mem.available_kb >= entry.min_ram_kb * 3 / 2 {
        Badge::RunsFast
    } else if mem.available_kb >= entry.min_ram_kb {
        Badge::TightFit
    } else {
        Badge::ExceedsRam
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const FIXTURE: &str = r#"{"models":[
        {"id":"tiny","url":"http://x/tiny.gguf","params_b":1.1,"quant":"Q4_K_M","min_ram_kb":2000000},
        {"id":"mid","url":"http://x/mid.gguf","params_b":3.0,"quant":"Q4_K_M","min_ram_kb":5000000}
    ]}"#;

    fn mem(avail: u64) -> MemInfo {
        MemInfo {
            total_kb: avail,
            available_kb: avail,
        }
    }

    #[test]
    fn parses_and_finds() {
        let m = Manifest::from_json(FIXTURE).unwrap();
        assert_eq!(m.models.len(), 2);
        assert_eq!(m.find("mid").unwrap().quant, "Q4_K_M");
        assert!(m.find("nope").is_none());
    }

    #[test]
    fn bundled_is_valid() {
        assert!(!Manifest::bundled().models.is_empty());
    }

    #[test]
    fn badge_edges() {
        let m = Manifest::from_json(FIXTURE).unwrap();
        let tiny = m.find("tiny").unwrap();
        assert_eq!(badge(tiny, &mem(3000000)), Badge::RunsFast); // >= 1.5x
        assert_eq!(badge(tiny, &mem(2000000)), Badge::TightFit); // == min
        assert_eq!(badge(tiny, &mem(1999999)), Badge::ExceedsRam);
    }

    #[tokio::test]
    async fn load_falls_back_offline() {
        let dir = std::env::temp_dir();
        let cache = dir.join(format!("mdb-manifest-{}.json", std::process::id()));
        let _ = tokio::fs::remove_file(&cache).await;
        // Nothing listens on port 9: fast refusal, no cache, no network.
        let m = load("http://127.0.0.1:9/manifest.json", &cache).await;
        assert!(!m.models.is_empty());
        let _ = tokio::fs::remove_file(&cache).await;
    }
}
