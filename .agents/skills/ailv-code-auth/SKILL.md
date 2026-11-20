---
name: ailv-code-auth
description: "Authentication is the most-broken OWASP category; one shared login path removes the whole class."
sources:
  - title: OAuth 2.0 RFC 6749
    url: https://www.rfc-editor.org/rfc/rfc6749
  - title: NIST SP 800-63B
    url: https://pages.nist.gov/800-63-3/sp800-63b.html
helper: scripts/helper.py
example: examples/output.md
---

# Login and permissions

`ailv-code-auth` (Login and permissions): Logins use signed cookies (built into Starlette — one secret key, no extra package). Sign in with Google uses authlib. Services talking to each other use JWTs via pyjwt. Passwords are checked with bcrypt via passlib — never write your own password check, because a wrong one fails silently and an agent will not notice. For every action, check the permission at the boundary and default to deny: never trust a role or user id sent by the client, always re-check it on the server. If the prescribed stack has no bcrypt/passlib, use the platform KDF (scrypt, PBKDF2) with a per-password salt and timing-safe compare — never a bare hash, never your own construction.

## Checks

- sessions are signed cookies
- passwords via bcrypt only
- permission checked per action, default deny
