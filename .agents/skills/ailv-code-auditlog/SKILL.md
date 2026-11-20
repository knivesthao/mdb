---
name: ailv-code-auditlog
description: "Debug logs are not audit logs — auditors ask who did what, and noise is not an answer."
sources:
  - title: NIST SP 800-92 log management
    url: https://csrc.nist.gov/pubs/sp/800/92/final
helper: scripts/helper.py
example: examples/output.md
---

# Immutable actor-action-target trail

`ailv-code-auditlog` (Immutable actor-action-target trail): Record actor, action, target, and timestamp as immutable events — debug logs are not audit logs (break-in detection lives in ailv-code-logging). Any app with more than one user role — or with money, permissions, or exports — needs this whether or not HIPAA applies; regulated data only makes mandatory what multi-user accountability already requires. Keep the trail append-only with a retention policy and export for auditors. Log permission changes, data exports, and impersonation sessions first; those are the rows auditors ask for. Name the agent in the actor field — 'which agent did this' must be answerable without asking anyone.

## Checks

- immutable actor-action-target events
- retention plus export
- permission and export actions covered
