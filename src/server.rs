//! OpenAI-compatible HTTP layer: `GET /health`, `GET /v1/models`, and
//! `POST /v1/chat/completions` with optional SSE streaming.
//!
//! `POST /v1/models/swap` is an MDB extension (not OpenAI) reserved for the
//! future Zed companion: hot-swaps the loaded model on the same endpoint.
//! Swaps serialize behind a mutex so in-flight requests finish first.

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
use tokio::{net::TcpListener, sync::Mutex};
use tokio_stream::wrappers::ReceiverStream;

use crate::inference::Backend;

#[derive(Clone)]
pub struct AppState {
    pub backend: Arc<dyn Backend>,
    pub swap_lock: Arc<Mutex<()>>,
}

impl AppState {
    pub fn new(backend: Arc<dyn Backend>) -> Self {
        Self {
            backend,
            swap_lock: Arc::new(Mutex::new(())),
        }
    }
}

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

#[derive(Serialize)]
struct ModelEntry {
    id: String,
    object: &'static str,
    owned_by: &'static str,
}

#[derive(Serialize)]
struct ModelList {
    object: &'static str,
    data: Vec<ModelEntry>,
}

#[derive(Deserialize)]
struct SwapRequest {
    model: String,
}

async fn health() -> &'static str {
    "ok"
}

async fn list_models(State(state): State<AppState>) -> impl IntoResponse {
    Json(ModelList {
        object: "list",
        data: vec![ModelEntry {
            id: state.backend.model_id(),
            object: "model",
            owned_by: "mdb",
        }],
    })
}

async fn swap_model(
    State(state): State<AppState>,
    Json(req): Json<SwapRequest>,
) -> Response {
    let _guard = state.swap_lock.lock().await;
    match state.backend.load(&req.model) {
        Ok(()) => Json(ModelEntry {
            id: state.backend.model_id(),
            object: "model",
            owned_by: "mdb",
        })
        .into_response(),
        Err(e) => (
            axum::http::StatusCode::INTERNAL_SERVER_ERROR,
            format!("swap failed: {e}"),
        )
            .into_response(),
    }
}

async fn chat_completions(
    State(state): State<AppState>,
    Json(req): Json<ChatRequest>,
) -> Response {
    let prompt = req
        .messages
        .last()
        .map(|m| m.content.clone())
        .unwrap_or_default();
    if req.stream {
        let (tx, rx) = tokio::sync::mpsc::channel::<Result<Event, Infallible>>(16);
        let backend = state.backend.clone();
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
        let content = state.backend.complete(&prompt).concat();
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

pub fn router(state: AppState) -> Router {
    Router::new()
        .route("/health", get(health))
        .route("/v1/models", get(list_models))
        .route("/v1/models/swap", post(swap_model))
        .route("/v1/chat/completions", post(chat_completions))
        .with_state(state)
}

pub async fn serve(listener: TcpListener, state: AppState) {
    axum::serve(listener, router(state)).await.unwrap();
}

pub async fn run(addr: &str, state: AppState) {
    let listener = TcpListener::bind(addr).await.unwrap();
    serve(listener, state).await;
}
