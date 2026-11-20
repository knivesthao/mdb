---
name: ailv-data-backfill
description: "Full-table reruns overload sources and double-write; unmarked ranges confuse readers."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Bounded throttled replays

`ailv-data-backfill` (Bounded throttled replays): Backfill bounded partitions, throttled — never full-table reruns that overload sources. Writers stay idempotent so a retried partition converges; mark overwritten ranges so readers never see half-old, half-new. Backfills run below production priority with their own quota.

## Checks

- bounded throttled partitions
- idempotent writers with markers
- below-prod priority
