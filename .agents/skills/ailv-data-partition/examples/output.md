# ailv-data-partition — worked example

Input: candidate keys `day` (cardinality 30) and `user_id`
(cardinality 2,000,000); file-size sample with 3 tiny files.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
PASS key=day cardinality=30 prunable
FAIL key=user_id cardinality=2000000 (tiny-file sprawl: use date)
FILES n=4 small=3 -> COMPACT scheduled
PASS
```

Low-cardinality date key prunes; the ID key is rejected; small files
are scheduled for compaction.
