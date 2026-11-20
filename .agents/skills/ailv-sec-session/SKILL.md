---
name: ailv-sec-session
description: "Long-lived JWTs with no revocation path stay valid after theft — the classic breach extender."
sources:
  - title: OWASP Session Management
    url: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
helper: scripts/helper.py
example: examples/output.md
---

# Short-lived revocable sessions

`ailv-sec-session` (Short-lived revocable sessions): Issue short-lived tokens with rotation and binding; keep server-side revocation so stolen sessions die on demand. Absolute lifetimes cap every session no matter how active. App login mechanics live in ailv-code-auth; this skill governs lifetimes and kill paths.

## Checks

- short-lived with rotation
- server-side revocation
- absolute lifetime caps
