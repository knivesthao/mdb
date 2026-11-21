//! Inference backend abstraction. The real `llama.cpp` FFI backend
//! (plan step 6, needs the NDK) implements [`Backend`]; until then the
//! server runs on [`MockBackend`] so the API is testable on any host.
//!
//! The trait is already shaped for Pro hot-swapping: `load` swaps the
//! weights behind the server's swap mutex (pause → free → load → re-pin
//! → resume), so the FFI backend drops in without changing the server.

use std::{io, sync::Mutex};

/// A text-completion backend. Returns the completion as a list of token
/// strings so the server can stream them as SSE events.
pub trait Backend: Send + Sync + 'static {
    fn complete(&self, prompt: &str) -> Vec<String>;
    fn model_id(&self) -> String;
    /// Swap the loaded weights to another model id.
    fn load(&self, model_id: &str) -> io::Result<()>;
}

/// Placeholder backend for host-side development and tests.
pub struct MockBackend {
    id: Mutex<String>,
}

impl MockBackend {
    pub fn new(model_id: &str) -> Self {
        Self {
            id: Mutex::new(model_id.to_string()),
        }
    }
}

impl Backend for MockBackend {
    fn complete(&self, prompt: &str) -> Vec<String> {
        let id = self.model_id();
        vec!["mock:".to_string(), format!(" [{id}]"), format!(" {prompt}"), " ok".to_string()]
    }

    fn model_id(&self) -> String {
        self.id.lock().unwrap().clone()
    }

    fn load(&self, model_id: &str) -> io::Result<()> {
        *self.id.lock().unwrap() = model_id.to_string();
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn mock_returns_tokens() {
        let b = MockBackend::new("tiny");
        let tokens = b.complete("hi");
        assert!(!tokens.is_empty());
        assert!(tokens.concat().contains("hi"));
        assert_eq!(b.model_id(), "tiny");
    }

    #[test]
    fn mock_hot_swap_changes_id() {
        let b = MockBackend::new("tiny");
        b.load("mid").unwrap();
        assert_eq!(b.model_id(), "mid");
        assert!(b.complete("x").concat().contains("mid"));
    }
}
