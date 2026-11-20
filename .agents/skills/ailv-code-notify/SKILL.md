---
name: ailv-code-notify
description: "Blocking inline sends turn every retry into a double-notify and every surge into a timeout."
sources:
  - title: Resend docs
    url: https://resend.com/docs
helper: scripts/helper.py
example: examples/output.md
---

# Queued templated sends, never blocking

`ailv-code-notify` (Queued templated sends, never blocking): Send every notification through a queue with a template — never blocking inline sends. Each user holds channel preferences (in-app, email, SMS, push); respect quiet hours with digested batches. Dedupe on event keys so retries never double-notify. Respect provider caps — template counts, destinations per call, send rates — and let the queue absorb them; a burst past the cap fails silently at the provider. Every outbound message carries a working unsubscribe; marketing and transactional never share a path.

## Checks

- queued templated sends only
- dedupe keys, no double-notify
- working unsubscribe
