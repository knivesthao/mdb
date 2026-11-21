//! Single-active-model store (plan step 3): the free tier holds one
//! GGUF at a time. The slot is `active.gguf` plus an `active.json`
//! sidecar recording which manifest id is loaded — the server reads the
//! sidecar for `/v1/models`. Downloading another model replaces the slot.

use std::{
    io,
    path::{Path, PathBuf},
};

pub const ACTIVE_NAME: &str = "active.gguf";
const SIDECAR_NAME: &str = "active.json";

/// Path of the single active model file, creating `dir` if needed.
pub fn active_path(dir: &Path) -> io::Result<PathBuf> {
    std::fs::create_dir_all(dir)?;
    Ok(dir.join(ACTIVE_NAME))
}

/// Record which manifest id occupies the slot.
pub fn record_model(dir: &Path, model_id: &str) -> io::Result<()> {
    std::fs::create_dir_all(dir)?;
    let body = format!("{{\"model_id\":{model_id:?}}}");
    std::fs::write(dir.join(SIDECAR_NAME), body)
}

/// Model id currently in the slot, or `None` when empty/unreadable.
pub fn read_model_id(dir: &Path) -> Option<String> {
    let text = std::fs::read_to_string(dir.join(SIDECAR_NAME)).ok()?;
    let v: serde_json::Value = serde_json::from_str(&text).ok()?;
    v.get("model_id")?.as_str().map(|s| s.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    fn dir() -> PathBuf {
        std::env::temp_dir().join(format!("mdb-store-{}", std::process::id()))
    }

    #[test]
    fn roundtrip_and_replace() {
        let d = dir();
        let _ = std::fs::remove_dir_all(&d);
        assert_eq!(read_model_id(&d), None);
        record_model(&d, "tiny").unwrap();
        assert_eq!(read_model_id(&d).as_deref(), Some("tiny"));
        // Replacing the slot overwrites the record.
        record_model(&d, "mid").unwrap();
        assert_eq!(read_model_id(&d).as_deref(), Some("mid"));
        assert!(active_path(&d).unwrap().ends_with(ACTIVE_NAME));
        let _ = std::fs::remove_dir_all(&d);
    }
}
