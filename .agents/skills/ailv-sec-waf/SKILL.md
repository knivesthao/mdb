---
name: ailv-sec-waf
description: "Monitor-only is decoration; copied defaults break legit users until someone disables everything."
sources:
  - title: OWASP Core Rule Set
    url: https://coreruleset.org/
helper: scripts/helper.py
example: examples/output.md
---

# Blocking rules tuned to real traffic

`ailv-sec-waf` (Blocking rules tuned to real traffic): Run WAF and input-filter rules in blocking mode tuned to legitimate traffic — monitor-only is decoration, and copied defaults break real users until someone disables the whole thing. Payload shapes live in ailv-code-injection; the WAF enforces what that skill defines. Exempt nothing sensitive from logging; tune on false positives weekly after launch.

## Checks

- blocking mode, tuned
- no monitor-only
- false positives tuned
