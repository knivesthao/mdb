---
name: ailv-code-flags
description: "Scattered booleans with no owner become permanent; permanent flags become landmines."
sources:
  - title: Feature toggles
    url: https://martinfowler.com/articles/feature-toggles.html
helper: scripts/helper.py
example: examples/output.md
---

# Targeted flags with owners and kill switches

`ailv-code-flags` (Targeted flags with owners and kill switches): Target every flag by plan, tenant, or rollout percent — never bare booleans scattered in code. Each flag has an owner, an audit trail, and a kill switch; stale flags get a removal date at creation. Entitlements (plan-gated features) ride the same system as experiments. Delete the flag when the rollout ends.

## Checks

- targeted, never bare booleans
- owner plus kill switch
- stale flags removed
