# Mobile AI Server — MVP Specification

## 1. Product Vision

An offline-first Android application built in **pure Rust** that turns any modern Android phone into a local AI inference server. The app features automated hardware profiling, intent-based model recommendations, and exposes an OpenAI-compatible API endpoint (`/v1/chat/completions`) so code editors like **Zed** can connect seamlessly over local Wi-Fi or a wired USB (`adb`) tunnel.

## 2. Core Tech Stack (Zero-JVM Overhead)

- **Core Inference Engine:** `llama.cpp` (compiled for ARM64 Android via the NDK, linked via Rust FFI).
- **Application & Server Runtime:** **Rust** (managing app logic, hardware scanning, and background orchestration).
- **Networking Daemon:** **Tokio** + **Axum** running an async HTTP/SSE server bound to `0.0.0.0:8080`.
- **UI Framework:** **Slint** (retained-mode reactive UI in Rust that draws zero CPU/GPU cycles when idle).
- **Hardware Acceleration:** Vulkan (GPU) and vendor NPU delegates (Qualcomm QNN / MediaTek NeuroPilot).

## 3. Simplified MVP User Flow

1. **Login Screen:** lightweight local email/token authentication stored securely in app-private storage.
2. **Onboarding & Hardware Scan:**
   - Automatically queries `/proc/meminfo` and chipset capabilities in the background.
   - User selects intent (*Code Completion, Chat/Writing, General Reasoning*).
   - App recommends a matching GGUF model within safe RAM limits, with an option for manual override.
3. **Active Server Dashboard:**
   - One-tap **"Start AI Server"** button.
   - Triggers a Foreground Service with a WakeLock to keep the app alive.
   - Displays local endpoints (`http://<phone-ip>:8080/v1` or `http://localhost:8080/v1` via USB) and live token metrics.

## 4. Development Roadmap (4 Weeks, 8 Hrs/Day Focus)

### Week 1: Core Inference & Rust FFI Integration

- **Days 1–2:** Set up the Android NDK toolchain and cross-compile `llama.cpp` for target `aarch64-linux-android`.
- **Days 3–5:** Build or integrate a Rust wrapper around `llama.cpp` via FFI. Test loading a small `.gguf` file and running text generation from a simple Rust test script.
- **Days 6–7:** Implement thread pinning (`pthread_setaffinity_np`) to lock tensor math strictly to the phone's Performance cores.

### Week 2: Hardware Profiling & Local API Server

- **Days 8–10:** Write the hardware scanner in Rust to parse `/proc/meminfo` and detect available RAM/SoC specs.
- **Days 11–13:** Set up **Tokio** and **Axum** to build an async HTTP server exposing a standard `/v1/chat/completions` OpenAI-compatible endpoint.
- **Day 14:** Connect the HTTP server to the inference engine using lock-free channels (`tokio::sync::mpsc`) for real-time Server-Sent Events (SSE) token streaming.

### Week 3: Android App Shell & UI

- **Days 15–17:** Integrate the **Slint** UI framework to build the login, hardware scan results, and intent-selection screens.
- **Days 18–19:** Implement the model downloader (handling large file streams, progress bars, and storage permissions).
- **Days 20–21:** Build the Android Foreground Service wrapper and WakeLock logic to ensure the server stays active when the screen dims.

### Week 4: IDE Connectivity & Polish

- **Days 22–24:** Configure **Zed** to point to your phone's local network IP or wired `localhost` tunnel (`adb reverse tcp:8080 tcp:8080`). Test live code completions.
- **Days 25–26:** Run performance benchmarks (tokens/sec tracking, thermal monitoring) and optimize memory buffers.
- **Days 27–28:** Final bug fixes, clean up error handling, and prepare the first local test build (.apk).

## 5. Day 1 Entry Point (Paused — Awaiting Go-Ahead)

- Toolchain check so far: `rustc`/`cargo` present, `cmake` present, Android NDK and `adb` not yet installed.
- Next when approved: `cargo init`, add Android targets, install NDK, vendor `llama.cpp`, wire FFI skeleton.
- Skills available in this repo: `.agents/skills/` (122 skills, mirrored from `dev/ADMAIS/aimeanslove`).
