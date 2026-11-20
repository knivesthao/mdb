---
name: ailv-ops-migrate
description: "Untested migrations with no rollback turn deploys into outages with no way back."
sources:
  - title: Alembic docs
    url: https://alembic.sqlalchemy.org/en/latest/
  - title: Parallel Change
    url: https://martinfowler.com/bliki/ParallelChange.html
helper: scripts/helper.py
example: examples/output.md
---

# Expand then contract, always reversible

`ailv-ops-migrate` (Expand then contract, always reversible): Version every schema change and run it automatically with the deploy. Expand then contract: add nullable, backfill, constrain, drop — readers never see a half-migrated schema. Every migration reverses or pairs with its undo; never edit an applied migration, only add the next one. Dry-run against prod-shaped data before touching prod.

## Checks

- expand-contract, never half-schemas
- reversible or paired
- dry-run on prod-shaped data
