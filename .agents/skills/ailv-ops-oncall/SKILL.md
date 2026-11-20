---
name: ailv-ops-oncall
description: "The single-hero pager with no notes guarantees the same incident repeats."
sources:
  - title: Site Reliability Engineering
    url: https://sre.google/books/
helper: scripts/helper.py
example: examples/output.md
---

# Rotation, runbooks, tracked postmortems

`ailv-ops-oncall` (Rotation, runbooks, tracked postmortems): Page a scheduled rotation with escalation paths and severity levels — never a single hero with no notes (page-worthy symptoms live in ailv-ops-observe). Every page links its runbook; pages without runbooks get written during the incident review. Blameless postmortems within days, action items tracked to done — the review nobody reads is the incident that repeats.

## Checks

- scheduled rotation with escalation
- runbook per page
- postmortems tracked to done
