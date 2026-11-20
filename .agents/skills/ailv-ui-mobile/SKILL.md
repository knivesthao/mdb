---
name: ailv-ui-mobile
description: "One language and zero client state means the agent writes every feature once and it ships to both app stores."
sources:
  - title: Capacitor docs
    url: https://capacitorjs.com/docs
helper: scripts/helper.py
example: examples/output.md
---

# Mobile: FastAPI + HTMX + Tailwind + Capacitor

`ailv-ui-mobile` (Mobile: FastAPI + HTMX + Tailwind + Capacitor): Build mobile apps as server-rendered HTML: FastAPI routes return fragments, HTMX attributes (hx-get/hx-target) give SPA behavior with near-zero JavaScript, Tailwind utilities handle responsive layout inline, Capacitor wraps the mobile viewport into iOS/Android shells. No client state, no fetch calls, no Swift/Kotlin.  If the project already uses a different mobile stack, do not create this skill at all — skip it.

## Checks

- zero hand-written fetch calls
- no client-side state store
- layout verified at 360px width
