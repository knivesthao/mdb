---
name: ailv-data-partition
description: "High-cardinality partitions spawn thousands of tiny files that slow every reader."
sources:
  - title: PostgreSQL partitioning
    url: https://www.postgresql.org/docs/current/ddl-partitioning.html
  - title: Delta Lake protocol
    url: https://github.com/delta-io/delta/blob/master/PROTOCOL.md
helper: scripts/helper.py
example: examples/output.md
---

# Prunable keys, no tiny files

`ailv-data-partition` (Prunable keys, no tiny files): Partition by low-cardinality date or key so queries prune whole ranges. Never high-cardinality IDs — they spawn thousands of tiny files that slow every reader. Target files sized for the reader (tens to hundreds of MB); compact the small ones on a schedule.

## Checks

- prunable low-cardinality keys
- no tiny-file sprawl
- compaction scheduled
