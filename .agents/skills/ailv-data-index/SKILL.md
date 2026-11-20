---
name: ailv-data-index
description: "Pipelines fail in the same three places — landing, ordering, replay — map first."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Data work: pick data skills

`ailv-data-index` (Data work: pick data skills): Your data skills each do one job — never read them all. Collection strategy → ailv-data-collect. Landing events exactly once → ailv-data-ingest. Ordering tasks with retries and stall alerts → ailv-data-orchestrate. Batch transforms → ailv-data-etl. Schemas and evolution → ailv-data-contracts. Data representation → ailv-data-model. Backfill and replay → ailv-data-backfill. CDC → ailv-data-cdc. Quality gates → ailv-data-quality. Partitioning → ailv-data-partition. Retention → ailv-data-retain. Streams → ailv-data-streams. Lineage → ailv-data-lineage. Upserts → ailv-data-upserts. Concurrent writers → ailv-data-concurrency. Shared metric definitions → ailv-data-metrics. Finding personal data → ailv-data-pii. Skip everything else.

## Checks

- only matched data skills are read
- repeat patterns banked, not pasted
