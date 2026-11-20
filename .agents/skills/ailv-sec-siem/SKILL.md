---
name: ailv-sec-siem
description: "Logs nobody verifies won't survive scrutiny; alert floods train analysts to ignore the one that matters."
sources:
  - title: NIST SP 800-92 log management
    url: https://csrc.nist.gov/pubs/sp/800/92/final
helper: scripts/helper.py
example: examples/output.md
---

# Tamper-evident logs analysts can trust

`ailv-sec-siem` (Tamper-evident logs analysts can trust): Aggregate auth, admin, and data-access events into tamper-evident searchable storage — and test the integrity, because logs nobody verifies won't survive scrutiny (product audit trails live in ailv-code-auditlog). Tune alerts to analyst capacity; unactioned floods train everyone to ignore the one that matters.

## Checks

- tamper-evident with tested integrity
- alerts tuned to capacity
