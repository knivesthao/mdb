use std::sync::Arc;

use mobileaiserver::{
    inference::MockBackend,
    model_store,
    server::{self, AppState},
};

#[tokio::main]
async fn main() {
    let data_dir = std::path::Path::new("data");
    let model_id = model_store::read_model_id(data_dir).unwrap_or_else(|| "none".to_string());
    let state = AppState::new(Arc::new(MockBackend::new(&model_id)));
    server::run("0.0.0.0:8080", state).await;
}
