//! Black-box HTTP tests: boot the real server on an ephemeral port and
//! talk to it over raw TCP, so no HTTP client dependency is needed.

use std::sync::Arc;
use std::time::Duration;

use mobileaiserver::{
    inference::MockBackend,
    server::{self, AppState},
};
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::{TcpListener, TcpStream};

fn state() -> AppState {
    AppState::new(Arc::new(MockBackend::new("test-model")))
}

async fn boot() -> std::net::SocketAddr {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    tokio::spawn(server::serve(listener, state()));
    // Give the accept loop a moment to start.
    tokio::time::sleep(Duration::from_millis(100)).await;
    addr
}

async fn round_trip(addr: std::net::SocketAddr, request: &str) -> String {
    let mut stream = TcpStream::connect(addr).await.unwrap();
    stream.write_all(request.as_bytes()).await.unwrap();
    let mut buf = Vec::new();
    stream.read_to_end(&mut buf).await.unwrap();
    String::from_utf8_lossy(&buf).into_owned()
}

fn post(path: &str, body: &str) -> String {
    format!(
        "POST {path} HTTP/1.1\r\nHost: x\r\nContent-Type: application/json\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
        body.len(),
        body
    )
}

#[tokio::test]
async fn health_returns_ok() {
    let addr = boot().await;
    let res = round_trip(
        addr,
        "GET /health HTTP/1.1\r\nHost: x\r\nConnection: close\r\n\r\n",
    )
    .await;
    assert!(res.starts_with("HTTP/1.1 200"), "got: {res}");
    assert!(res.ends_with("ok"));
}

#[tokio::test]
async fn chat_completion_returns_json() {
    let addr = boot().await;
    let body = r#"{"model":"test","messages":[{"role":"user","content":"hi"}]}"#;
    let res = round_trip(addr, &post("/v1/chat/completions", body)).await;
    assert!(res.starts_with("HTTP/1.1 200"), "got: {res}");
    let json = res.split("\r\n\r\n").nth(1).unwrap();
    assert!(json.contains("chat.completion"), "got: {json}");
    assert!(json.contains("hi"), "got: {json}");
}

#[tokio::test]
async fn chat_completion_streams_sse() {
    let addr = boot().await;
    let body =
        r#"{"model":"test","stream":true,"messages":[{"role":"user","content":"hi"}]}"#;
    let res = round_trip(addr, &post("/v1/chat/completions", body)).await;
    assert!(res.starts_with("HTTP/1.1 200"), "got: {res}");
    assert!(res.contains("text/event-stream"), "got: {res}");
    assert!(res.contains("data:"), "got: {res}");
    assert!(res.contains("[DONE]"), "got: {res}");
}

#[tokio::test]
async fn models_lists_loaded_model() {
    let addr = boot().await;
    let res = round_trip(
        addr,
        "GET /v1/models HTTP/1.1\r\nHost: x\r\nConnection: close\r\n\r\n",
    )
    .await;
    assert!(res.starts_with("HTTP/1.1 200"), "got: {res}");
    assert!(res.contains("test-model"), "got: {res}");
}

#[tokio::test]
async fn swap_changes_loaded_model() {
    let addr = boot().await;
    let res = round_trip(addr, &post("/v1/models/swap", r#"{"model":"mid"}"#)).await;
    assert!(res.starts_with("HTTP/1.1 200"), "got: {res}");
    assert!(res.contains("mid"), "got: {res}");
    // Same endpoint now serves the new model.
    let res = round_trip(
        addr,
        "GET /v1/models HTTP/1.1\r\nHost: x\r\nConnection: close\r\n\r\n",
    )
    .await;
    assert!(res.contains("mid"), "got: {res}");
}
