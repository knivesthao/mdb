---
name: ailv-data-orchestrate
description: "Chained cron fails silently at 3am — explicit deps with stall alerts fail loudly instead."
sources:
  - title: Airflow docs
    url: https://airflow.apache.org/docs/
helper: scripts/helper.py
example: examples/output.md
---

# Pipelines as DAGs with stall SLAs

`ailv-data-orchestrate` (Pipelines as DAGs with stall SLAs): Model every pipeline as a DAG with explicit dependencies — never chained cron that fails silently. Each task retries with backoff and declares its own stall SLA; breach pages, success stays quiet. Tasks must be idempotent so reruns converge. The scheduler owns ordering, retries, and alerts; the task owns one transform.

## Checks

- deps explicit, no chained cron
- stall SLAs page, success quiet
- tasks idempotent
