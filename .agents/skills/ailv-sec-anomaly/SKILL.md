---
name: ailv-sec-anomaly
description: "Set-once thresholds decay into false-positive floods that bury the real attack."
sources:
  - title: MITRE ATT&CK
    url: https://attack.mitre.org/
helper: scripts/helper.py
example: examples/output.md
---

# Baselines retuned, sharp signals page

`ailv-sec-anomaly` (Baselines retuned, sharp signals page): Baseline user, endpoint, and network behavior, then continuously retune — thresholds set once decay into false-positive floods everyone ignores. Promote only impossible-travel and lateral-movement class signals to pages; the rest stays in analyst review queues.

## Checks

- baselines with continuous retuning
- only sharp signals page
