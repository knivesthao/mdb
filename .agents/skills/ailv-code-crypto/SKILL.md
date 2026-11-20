---
name: ailv-code-crypto
description: "Homegrown crypto fails silently; platform crypto fails loudly and rarely."
sources:
  - title: Let's Encrypt docs
    url: https://letsencrypt.org/docs/
  - title: libsodium docs
    url: https://doc.libsodium.org/
helper: scripts/helper.py
example: examples/output.md
---

# No homegrown crypto

`ailv-code-crypto` (No homegrown crypto): Use vetted crypto only: TLS for data in motion, platform encryption (KMS, age, or libsodium) for data at rest — never a hand-rolled cipher. Secrets live in environment variables, never in code or logs. Passwords are hashed, not encrypted (see ailv-code-auth); API tokens are random, scoped, and expire.

## Checks

- no hand-rolled ciphers
- no secret in code or logs
- tokens expire and are scoped
