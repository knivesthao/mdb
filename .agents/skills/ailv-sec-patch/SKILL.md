---
name: ailv-sec-patch
description: "Exempted exec and legacy machines become the persistent foothold."
sources:
  - title: CIS Benchmarks
    url: https://www.cisecurity.org/cis-benchmarks
helper: scripts/helper.py
example: examples/output.md
---

# Fleet-wide patching, no exemptions

`ailv-sec-patch` (Fleet-wide patching, no exemptions): Push OS, browser, and agent updates fleet-wide with CIS baselines — including exec and legacy machines, because exemptions become the persistent foothold. Patch windows are scheduled and measured; unpatched stragglers page their owners.

## Checks

- fleet-wide including exemptions
- measured patch windows
