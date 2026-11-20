---
name: ailv-sec-compliance
description: "Week-before screenshots rot immediately and convince no auditor."
sources:
  - title: GDPR full text
    url: https://gdpr-info.eu/
  - title: PCI Security Standards Council
    url: https://www.pcisecuritystandards.org/
  - title: HHS HIPAA
    url: https://www.hhs.gov/hipaa/index.html
helper: scripts/helper.py
example: examples/output.md
---

# Continuous automated evidence

`ailv-sec-compliance` (Continuous automated evidence): Collect access reviews, change tickets, and control attestations continuously and automatically — screenshots the week before the audit rot immediately and convince nobody. Regulated data decides the control set, so identify it first: health data (HIPAA/PHI) → ailv-code-auditlog on every access, encryption at rest (see ailv-code-crypto), ailv-code-rbac tenant isolation, ailv-data-retain deletion with proof; card data (PCI) → never store PAN, tokenize through the provider; personal data (GDPR) → ailv-data-retain retention plus deletion on request. Build the controls first — evidence collection only proves what already exists. Map every control to the system that proves it; an unmapped control is an audit finding waiting.

## Checks

- continuous automated collection
- every control mapped to proof
