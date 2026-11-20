//! Inference backend abstraction. The real `llama.cpp` FFI backend
//! (plan step 6, needs the NDK) implements [`Backend`]; until then the
//! server runs on [`MockBackend`] so the API is testable on any host.

/// A text-completion backend. Returns the completion as a list of token
/// strings so the server can stream them as SSE events.
pub trait Backend: Send + Sync + 'static {
    fn complete(&self, prompt: &str) -> Vec<String>;
}

/// Placeholder backend for host-side development and tests.
pub struct MockBackend;

impl Backend for MockBackend {
    fn complete(&self, prompt: &str) -> Vec<String> {
        vec![
            "mock:".to_string(),
            format!(" {prompt}"),
            " ok".to_string(),
        ]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn mock_returns_tokens() {
        let tokens = MockBackend.complete("hi");
        assert!(!tokens.is_empty());
        assert!(tokens.concat().contains("hi"));
    }
}
