# MDB (Mobile Dev Bridge) — Specification (merged)

## 1. Product Vision

An offline-first Android application built in **pure Rust** that turns any modern Android phone into a local AI inference server. Unlike standalone chat-client apps, MDB treats the phone as a **headless server node** for desktop code editors (starting with **Zed**): open the app once, tap start, put the phone down, and code from the laptop over local Wi-Fi or a wired USB (`adb`) tunnel. Automated hardware profiling and intent-based model recommendations gate everything to OOM-safe choices.

## 2. Core Tech Stack (Zero-JVM Overhead)

- **Core Inference Engine:** `llama.cpp` (ARM64 Android via the NDK, linked via Rust FFI).
- **Application & Server Runtime:** **Rust** (app logic, hardware scanning, model registry, background tasks).
- **Networking Daemon:** **Tokio** + **Axum** async HTTP/SSE server on `0.0.0.0:8080`. Minimal feature sets only (`tokio` without `full`; size-first release profile: `opt-level = "z"`, `lto = "fat"`, `strip`).
- **UI Framework:** **Slint** (retained-mode, zero idle cycles).
- **Hardware Acceleration:** Vulkan (GPU) and vendor NPU delegates (Qualcomm QNN / MediaTek NeuroPilot).
- **Discovery:** `mdns-sd` advertising `mdb.local:8080`; USB via `adb reverse tcp:8080 tcp:8080`.

## 3. Product Tiers

### Free Tier: Zero-Friction Local Server (No Account Required)

- **No login.** The app launches straight into hardware detection and model setup. There is no working sign-in in Phase 1; the UI keeps only a dormant Pro placeholder.
- **Single active model:** one GGUF file at a time. Downloading another model replaces the existing file.

### Pro Tier (Phase 2 — not built yet)

- Accounts exist **only** for paid users; one verification path will be chosen for Phase 2 (recommended: license key / email magic link first, store receipts later).
- **Model Vault:** multiple stored GGUFs, one in RAM at a time. Hot-swap pauses the Tokio request queue, frees the model, loads the new weights, re-pins threads, resumes on the same endpoint. Encrypted Pro token cached locally (Android Keystore).

## 4. User Flow & Screens

1. **Hardware Auto-Scan & Intent Selection (immediate entry):** background Rust worker parses `/proc/meminfo`, core topology, Vulkan properties. Model choices come from a **remote JSON manifest** (verified GGUF URLs, sizes, quants, RAM requirements) with a bundled fallback, updatable over-the-air.
   - **Path A ("Help me choose"):** pick an intent (*Code Completion, Chat/Writing, Reasoning*); MDB filters the manifest by hardware tier and highlights the best fit.
   - **Path B ("I know what I want"):** searchable catalog with compatibility badges (`Runs Fast`, `Tight Fit`, `Exceeds RAM`) — a pure function of manifest + scanner data.
2. **Server Dashboard & Active Mode:** one-tap **"Start AI Server"**; Foreground Service + WakeLock so the OS doesn't kill it when the screen dims. Live tokens/sec, RAM usage, copyable endpoint URLs.

## 5. IDE Connectivity (Zed)

- OpenAI-compatible `POST /v1/chat/completions` (JSON + SSE streaming) and `GET /v1/models` (currently loaded model).
- Transports: local Wi-Fi/hotspot + mDNS (`mdb.local:8080`); USB `adb reverse` as the reliable low-jitter primary for testing.
- Zed uses its custom OpenAI-compatible provider settings. A companion Zed extension (live status, vault hot-swap trigger) is Phase 3.

## 6. Performance & Concurrency Guardrails

- Pre-allocated buffers / KV-cache at init (set via `llama.cpp` init params at FFI time — config, not our code).
- Thread pinning (`pthread_setaffinity_np`) onto Prime/Performance cores, isolated from the Tokio runtime.
- Lock-free token streaming via `tokio::sync::mpsc` → SSE.
- Hot-swap contract: swaps serialize against in-flight requests behind a mutex (pause → free → load → re-pin → resume).
- Keep the Rust core's public surface narrow and FFI-friendly — Phase 3 iOS goes through UniFFI, so no sprawling core API now.

## 7. Phased Rollout

- **Phase 1 (MVP):** Rust core, NDK `llama.cpp` FFI, hardware scanner, zero-login free tier (single model), JSON manifest, Axum OpenAI endpoint (`/v1/chat/completions`, `/v1/models`), mDNS/USB, Zed config.
- **Phase 2 (Pro):** one auth path, encrypted license cache, Model Vault storage + one-tap hot-swap.
- **Phase 3 (Ecosystem):** Zed companion extension, iOS port (shared Rust core via UniFFI + SwiftUI).

## 8. Deferred / Future Backlog (revisit explicitly — do not build in Phase 1)

- Pro auth method decision (license key / magic link vs store receipts) and Supabase-vs-static backend choice.
- Encrypted Pro token cache via Android Keystore.
- Vault multi-model storage UI + dashboard quick-switcher.
- Zed companion extension.
- iOS port (UniFFI + SwiftUI).
- HTTPS downloader + redirects (required before custom Hugging Face URL input works).
- FFI hot-swap body (needs NDK + phone).
- Notification muting / high-performance scheduling details in AI Server Mode.
- Benchmarks: tokens/sec tracking, thermal monitoring, memory-buffer tuning.

## 9. Build Notes (host-side, verified)

- `cargo test`: scanner, mock inference, affinity fallback, downloader (resume/progress), API black-box tests (`/health`, JSON + SSE completions) — green.
- `cargo build --bin mdb-ui`: Slint login/hardware/server tabs compile; visual check pending in VM.
- Done: Android target installed, `llama.cpp` vendored as submodule, trimmed async features, size-first release profile.
- Blocked on user/VM side: NDK + `adb` installs, phone deploy, Zed end-to-end, APK.
