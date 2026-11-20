---
name: ailv-sec-sso
description: "Permanent break-glass exceptions and legacy logins are the doors attackers walk through."
sources:
  - title: OpenID Connect
    url: https://openid.net/connect/
  - title: WebAuthn Level 3
    url: https://www.w3.org/TR/webauthn-3/
helper: scripts/helper.py
example: examples/output.md
---

# One IdP, expiring exceptions

`ailv-sec-sso` (One IdP, expiring exceptions): Route every login through one identity provider — workforce and enterprise customers alike (app basics live in ailv-code-auth). Require phishing-resistant MFA; expire legacy password-only logins and break-glass exceptions with a date, never permanently. Provision just-in-time on first login from verified domains; deprovision automatically on IdP removal. Every exception carries an owner, an expiry, and an audit trail.

## Checks

- one IdP, no permanent exceptions
- JIT provision, auto deprovision
- exceptions owned, expiring, audited
