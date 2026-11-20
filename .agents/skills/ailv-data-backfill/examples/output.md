# ailv-data-backfill — worked example

Input: bounded replay of 3 date partitions at 2 partitions/sec quota
(below production priority), then a retried partition.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
BACKFILL partition=2026-01-01 rows=2 marker=rewritten (throttled)
BACKFILL partition=2026-01-02 rows=2 marker=rewritten (throttled)
BACKFILL partition=2026-01-03 rows=2 marker=rewritten (throttled)
RERUN converges=True markers=3
PASS
```

Bounded throttled partitions, idempotent writers, ranges marked as
rewritten so readers never see half-old, half-new.
