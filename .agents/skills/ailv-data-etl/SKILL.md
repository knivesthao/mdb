---
name: ailv-data-etl
description: "Untested SQL with no idempotent reload turns every rerun into new duplicates."
sources:
  - title: dbt docs
    url: https://docs.getdbt.com/docs/build/projects
helper: scripts/helper.py
example: examples/output.md
---

# Tested transforms, idempotent reloads

`ailv-data-etl` (Tested transforms, idempotent reloads): Keep every transform in tested code with idempotent reloads — rerunning a date range converges, never duplicates. Business logic lives in reviewed, tested functions, not in untested SQL strings. Partition the reload unit by date so backfills touch days, not tables. Incremental loads that cannot partition by date need a unique key for merge-or-dedupe — without one, reruns duplicate.

## Checks

- transforms tested
- reloads idempotent by partition
- no untested SQL logic
- incremental loads carry a unique key
