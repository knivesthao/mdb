# ailv-data-orchestrate — worked example

Input: demo DAG `extract -> transform -> load` with per-task stall SLAs
of 60s; `load` takes 200s.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
ORDER extract -> transform -> load
OK task=extract elapsed=12s (quiet)
OK task=transform elapsed=30s (quiet)
STALL page task=load elapsed=200s sla=60s
RERUN idempotent: transform rerun converges (no dupes)
PASS
```

Explicit deps order the run, the stall pages, successes stay quiet.
