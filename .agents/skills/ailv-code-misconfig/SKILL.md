---
name: ailv-code-misconfig
description: "Most breaches walk through doors the defaults left open."
sources:
  - title: OWASP Secure Headers
    url: https://owasp.org/www-project-secure-headers/
  - title: MDN Content Security Policy
    url: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
helper: scripts/helper.py
example: examples/output.md
---

# Safe settings shipped

`ailv-code-misconfig` (Safe settings shipped): Ship with the safe settings on: debug and trace off in production, generic error pages that leak nothing, strict transport security and a content security policy, CORS allowlists instead of wildcards, and no default passwords or open admin pages. Review headers and flags on every deploy, not once.

## Checks

- debug off in production
- security headers set
- no defaults or wildcards
