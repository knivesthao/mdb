---
name: ailv-ops-iac
description: "Console click-ops leaves infra living in one engineer's head — unreviewed and unrepeatable."
sources:
  - title: Terraform docs
    url: https://developer.hashicorp.com/terraform/docs
helper: scripts/helper.py
example: examples/output.md
---

# Reproducible from a clean account

`ailv-ops-iac` (Reproducible from a clean account): Define every environment version-controlled and reproducible from a clean account — console click-ops is never the source of truth. Plan output reviews before applies on shared environments; drift detection runs on a schedule and pages when reality diverges. State files are locked and backed up like production data.

## Checks

- reproducible from clean account
- drift detection scheduled
- state locked and backed up
