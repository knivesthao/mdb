---
name: ailv-code-apikeys
description: "A leaked plaintext key database hands attackers access; god-mode scopes hand them everything."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Hashed, scoped, revocable keys

`ailv-code-apikeys` (Hashed, scoped, revocable keys): Store only hashes of customer API keys — a leaked database must not leak access. Scope every key least-privilege with per-key rate limits, rotation, and instant revocation. Show the secret once at creation, never again. Attribute every call to its key for metering and abuse tracing.

## Checks

- hashes stored, shown once
- scoped with per-key limits
- instant revocation
