# ailv-data-etl — worked example

Input: date-partitioned reload of day `2026-01-01` with 2 rows, then the
same reload run a second time.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
PASS test_transform
RELOAD day=2026-01-01 rows=2 after_rerun=2
PASS
CHECK incremental loads carry unique key: user_id present -> PASS
```

Rerunning a date range converges (2 rows, never duplicates); business
logic lives in a tested function, not a SQL string.
