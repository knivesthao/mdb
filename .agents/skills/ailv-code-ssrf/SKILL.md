---
name: ailv-code-ssrf
description: "A server that fetches arbitrary URLs becomes a proxy into your own network."
sources:
  - title: OWASP Top 10
    url: https://owasp.org/Top10/
helper: scripts/helper.py
example: examples/output.md
---

# Server fetches allowlisted

`ailv-code-ssrf` (Server fetches allowlisted): Never fetch a user-supplied URL from the server without an allowlist: block internal addresses and cloud metadata (169.254.169.254), resolve and re-check the host, and cap timeouts and response sizes. Prefer webhooks and signed callbacks over server-side fetching whenever the design allows.

## Checks

- user URLs allowlisted
- metadata IP blocked
- timeouts and size caps set
