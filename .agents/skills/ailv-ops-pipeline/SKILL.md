---
name: ailv-ops-pipeline
description: "Hand-rolled pipelines drift until the deploy that matters most is the one least tested."
sources:
  - title: GitHub Actions docs
    url: https://docs.github.com/en/actions
helper: scripts/helper.py
example: examples/output.md
---

# One template, gated deploys, one-button rollback

`ailv-ops-pipeline` (One template, gated deploys, one-button rollback): Deploy only from one shared templated pipeline — never hand-rolled per repo. Required gates in order: build, tests, security scan, plan-preview, approval for production. Mutations preview first: every mutating step publishes its plan — diff, SQL, target list — as a gate artifact before approval; no blind applies. The plan output is machine-readable so agents verify it and humans approve it, never prose describing what might happen. Every deploy links to its commit; every PR gets a preview environment (see ailv-ops-preview). Broadcast deploy start and finish as machine-readable trigger events (see ailv-ops-observe) so agents and rollouts react without polling. Rollback means redeploying the previous known-good artifact with one action — never a new build under fire. Block on critical scan findings; ticket the rest with SLAs. Deliver trigger events on a real bus with ordering, dedup, and replay — an event nobody reliably delivers is a log line with ambition.

## Checks

- one shared template, no hand-rolled pipes
- preview envs auto-stop
- rollback is one action on an old artifact
- mutating steps publish a machine-readable plan before approval
