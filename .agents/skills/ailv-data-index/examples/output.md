# ailv-data-index — worked example (router self-check)

Input: 4 task phrases routed to data skills by keyword; only matched
skills are read.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
PASS route 'backfill the partitions' -> ['ailv-data-backfill', 'ailv-data-partition']
PASS route 'check quality gates' -> ['ailv-data-quality']
PASS route 'find pii in notes' -> ['ailv-data-pii']
PASS route 'stream late events' -> ['ailv-data-streams']
CHECK only matched skills read, rest skipped -> PASS
PASS
```
