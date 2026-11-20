use std::sync::Arc;

use mobileaiserver::{inference::MockBackend, server};

#[tokio::main]
async fn main() {
    server::run("0.0.0.0:8080", Arc::new(MockBackend)).await;
}
