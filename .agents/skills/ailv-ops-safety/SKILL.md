---
name: ailv-ops-safety
description: "Fast agents with prod access convert mistakes into outages at machine speed."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Blast radius first, speed second

`ailv-ops-safety` (Blast radius first, speed second): Scope every agent's credentials least-privilege: an agent touches only its area's deploy, data, and secrets — IAM, DNS, billing, prod data, and root credentials are never in an agent's reach. Destructive ops (data deletes, infra teardown, mass revocation) never execute without a human's approval first — no agent approver, no emergency bypass of the human, only a faster path to reach them. An actor whose deploys fail twice in a row loses deploy rights automatically, like a drained host, until a human reinstates them. Cap what agents may spend: budgets with alerts and kill switches on agent-driven cloud actions.

## Checks

- agents scoped, never-touch list enforced
- destructive ops wait for human approval first
- failing actors auto-drained, spend capped
