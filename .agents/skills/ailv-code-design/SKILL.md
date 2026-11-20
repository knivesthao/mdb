---
name: ailv-code-design
description: "Missing controls can't be patched in later without redesigning the feature."
sources:
  - title: OWASP Threat Modeling
    url: https://owasp.org/www-community/Threat_Modeling_Process
helper: scripts/helper.py
example: examples/output.md
---

# Abuse story first

`ailv-code-design` (Abuse story first): For each feature, ask how it is abused before asking how it is used: who pays for heavy use, who is hurt by bad input. Default to deny, grant least privilege, rate-limit costly endpoints, and cap upload and response sizes. A feature without an abuse story is not designed yet.

## Checks

- abuse story per feature
- default deny
- costly endpoints rate-limited
