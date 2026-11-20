---
name: ailv-ops-index
description: "Deploys and pages follow the same gates everywhere — map first, improvise never."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Ops work: pick ops skills

`ailv-ops-index` (Ops work: pick ops skills): Your ops skills each do one job — never read them all. Build-test-deploy gates → ailv-ops-pipeline. Logs, metrics, traces, paging → ailv-ops-observe. Preview envs → ailv-ops-preview. Migrations → ailv-ops-migrate. Rollouts → ailv-ops-rollout. Secrets at runtime → ailv-ops-secrets. Backups and restore drills → ailv-ops-backup. Infra as code → ailv-ops-iac. Autoscaling → ailv-ops-scale. Health probes → ailv-ops-probes. Rotations and postmortems → ailv-ops-oncall. Destructive ops and failing actors → ailv-ops-safety. Cutting a release → ailv-ops-release. Two or more agents on one deploy or codebase → ailv-ops-coordinate. Humans verify the rollout dashboard and the drill record — never the procedure text; agents read the plan ledger and the deploy receipt instead. Skip everything else.

## Checks

- only matched ops skills are read
- unproven ops work never ships
