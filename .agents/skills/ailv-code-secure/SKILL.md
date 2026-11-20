---
name: ailv-code-secure
description: "Insecure code fails late and expensively; validated boundaries fail fast on the first bad input."
sources:
  - title: OWASP Top 10
    url: https://owasp.org/Top10/
helper: scripts/helper.py
example: examples/output.md
---

# Secure by default

`ailv-code-secure` (Secure by default): Validate every input at the boundary

## Checks

- all inputs validated
- no eval/innerHTML with raw input
- no secret in repo
