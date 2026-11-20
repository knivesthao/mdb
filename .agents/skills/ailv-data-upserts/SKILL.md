---
name: ailv-data-upserts
description: "Full overwrites waste the cluster and lose concurrent writes; lost watermarks drift forever."
sources:
  - title: PostgreSQL INSERT upsert
    url: https://www.postgresql.org/docs/current/sql-insert.html
helper: scripts/helper.py
example: examples/output.md
---

# Merge by keys, never full overwrite

`ailv-data-upserts` (Merge by keys, never full overwrite): Merge only new or changed rows by keys or watermarks — naive full overwrites waste the cluster and lose concurrent writes. Watermarks advance only after the merge commits; a crashed load resumes from the last committed mark, never from zero.

## Checks

- keyed merges, no full overwrites
- watermarks advance on commit
