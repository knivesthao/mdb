//! OpenAI-compatible HTTP layer: `GET /health` and
//! `POST /v1/chat/completions` with optional SSE streaming.

use std::{convert::Infallible, sync::Arc};

use axum::{
    Json, Router,
    extract::State,
    response::{
        IntoResponse, Response,
        sse::{Event, KeepAlive, Sse},
    },
    routing::{get, post},
};
use serde::{Deserialize, Serialize};
use tokio::net::TcpListener;
use tokio::sync::mpsc;
use tokio_stream::wrappers::ReceiverStream;

use crate::inference::Backend;

#[derive(Deserialize)]
struct ChatMessage {
    content: String,
}

#[derive(Deserialize)]
struct ChatRequest {
    model: String,
    messages: Vec<ChatMessage>,
    #[serde(default)]
    stream: bool,
}

#[derive(Serialize)]
struct ChatChoice {
    message: ChatMessageOut,
}

#[derive(Serialize)]
struct ChatMessageOut {
    role: &'static str,
    content: String,
}

#[derive(Serialize)]
struct ChatResponse {
    object: &'static str,
    model: String,
    choices: Vec<ChatChoice>,
}

async fn health() -> &'static str {
    "ok"
}

async fn chat_completions(
    State(backend): State<Arc<dyn Backend>>,
    Json(req): Json<ChatRequest>,
) -> Response {
    let prompt = req
        .messages
        .last()
        .map(|m| m.content.clone())
        .unwrap_or_default();
    if req.stream {
        let (tx, rx) = mpsc::channel::<Result<Event, Infallible>>(16);
        tokio::spawn(async move {
            for token in backend.complete(&prompt) {
                let event = Event::default().data(token);
                if tx.send(Ok(event)).await.is_err() {
                    return;
                }
            }
            let _ = tx.send(Ok(Event::default().data("[DONE]"))).await;
        });
        Sse::new(ReceiverStream::new(rx))
            .keep_alive(KeepAlive::default())
            .into_response()
    } else {
        let content = backend.complete(&prompt).concat();
        Json(ChatResponse {
            object: "chat.completion",
            model: req.model,
            choices: vec![ChatChoice {
                message: ChatMessageOut {
                    role: "assistant",
                    content,
                },
            }],
        })
        .into_response()
    }
}

pub fn router(backend: Arc<dyn Backend>) -> Router {
    Router::new()
        .route("/health", get(health))
        .route("/v1/chat/completions", post(chat_completions))
        .with_state(backend)
}

pub async fn serve(listener: TcpListener, backend: Arc<dyn Backend>) {
    axum::serve(listener, router(backend)).await.unwrap();
}

pub async fn run(addr: &str, backend: Arc<dyn Backend>) {
    let listener = TcpListener::bind(addr).await.unwrap();
    serve(listener, backend).await;
}
