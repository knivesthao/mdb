---
name: ailv-sec-runbooks
description: "Undrilled runbooks mean improvisation during the breach that matters."
sources:
  - title: NIST SP 800-61 incident handling
    url: https://csrc.nist.gov/pubs/sp/800/61/r2/final
helper: scripts/helper.py
example: examples/output.md
---

# Containment playbooks that get drilled

`ailv-sec-runbooks` (Containment playbooks that get drilled): Write containment playbooks per breach class — isolation, credential rotation, customer notice — and drill them (rotation process lives in ailv-ops-oncall). Severity levels and escalation paths are decided in advance, not mid-breach. Every drill updates the playbook or it rots.

## Checks

- containment per breach class
- drilled, not shelved
- drills update the playbook
