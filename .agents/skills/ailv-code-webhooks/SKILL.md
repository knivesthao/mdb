---
name: ailv-code-webhooks
description: "Unsigned fire-and-forget posts leave customers debugging your deliveries with no tools."
sources:
  - title: Stripe webhooks
    url: https://docs.stripe.com/webhooks
  - title: Svix docs
    url: https://docs.svix.com/
helper: scripts/helper.py
example: examples/output.md
---

# Signed payloads with replay

`ailv-code-webhooks` (Signed payloads with replay): Sign every outbound payload so receivers can verify it; version the event schema. Retry with backoff on failure and keep a delivery log per destination with replay — customers debug with replays, not with your logs. Receivers dedup on event ids, so sending twice is safe. Never fire-and-forget.

## Checks

- signed versioned payloads
- retry plus replay per destination
- delivery logs customer-visible
