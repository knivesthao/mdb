//! Hardware profiling: parse `/proc/meminfo` and recommend a model
//! class that fits in RAM for the user's intent.

/// Memory figures parsed from `/proc/meminfo`, in KiB.
#[derive(Debug, PartialEq, Eq)]
pub struct MemInfo {
    pub total_kb: u64,
    pub available_kb: u64,
}

/// Parse the `MemTotal` and `MemAvailable` lines out of meminfo text.
/// Returns `None` when either line is missing or malformed.
pub fn parse_meminfo(text: &str) -> Option<MemInfo> {
    let mut total = None;
    let mut available = None;
    for line in text.lines() {
        let mut parts = line.split_whitespace();
        match parts.next() {
            Some("MemTotal:") => total = parts.next()?.parse().ok(),
            Some("MemAvailable:") => available = parts.next()?.parse().ok(),
            _ => {}
        }
    }
    Some(MemInfo {
        total_kb: total?,
        available_kb: available?,
    })
}

/// What the user wants the server for. Drives the recommendation.
pub enum Intent {
    CodeCompletion,
    ChatWriting,
    GeneralReasoning,
}

/// Recommend a model class that fits in ~60% of total RAM, tuned by intent.
/// Returns a static model id the downloader can resolve later.
pub fn recommend(total_kb: u64, intent: Intent) -> &'static str {
    const GB: u64 = 1024 * 1024;
    match (total_kb, intent) {
        (t, Intent::CodeCompletion) if t < 4 * GB => "qwen2.5-coder-0.5b",
        (t, Intent::CodeCompletion) if t < 8 * GB => "qwen2.5-coder-1.5b",
        (_, Intent::CodeCompletion) => "qwen2.5-coder-3b",
        (t, _) if t < 4 * GB => "tinyllama-1.1b",
        (t, Intent::ChatWriting) if t < 8 * GB => "llama-3.2-1b",
        (t, Intent::GeneralReasoning) if t < 8 * GB => "llama-3.2-1b",
        (t, Intent::ChatWriting) => {
            let _ = t;
            "llama-3.2-3b"
        }
        (t, Intent::GeneralReasoning) => {
            let _ = t;
            "qwen2.5-3b"
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const SAMPLE: &str = "MemTotal:        7701032 kB\n\
                          MemFree:          842336 kB\n\
                          MemAvailable:     4200888 kB\n";

    #[test]
    fn parses_sample_meminfo() {
        assert_eq!(
            parse_meminfo(SAMPLE),
            Some(MemInfo {
                total_kb: 7701032,
                available_kb: 4200888,
            })
        );
    }

    #[test]
    fn missing_lines_return_none() {
        assert_eq!(parse_meminfo("MemTotal: 100 kB\n"), None);
        assert_eq!(parse_meminfo("garbage"), None);
    }

    #[test]
    fn low_ram_recommends_tiny_models() {
        const GB: u64 = 1024 * 1024;
        assert_eq!(
            recommend(2 * GB, Intent::CodeCompletion),
            "qwen2.5-coder-0.5b"
        );
        assert_eq!(recommend(2 * GB, Intent::ChatWriting), "tinyllama-1.1b");
    }

    #[test]
    fn high_ram_recommends_bigger_models() {
        const GB: u64 = 1024 * 1024;
        assert_eq!(
            recommend(12 * GB, Intent::CodeCompletion),
            "qwen2.5-coder-3b"
        );
        assert_eq!(recommend(12 * GB, Intent::ChatWriting), "llama-3.2-3b");
        assert_eq!(
            recommend(12 * GB, Intent::GeneralReasoning),
            "qwen2.5-3b"
        );
    }
}
