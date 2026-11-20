# ailv-data-concurrency — worked example

Input: two writers racing on one row with optimistic locking; the loser
retries the whole transaction.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
A commit=True B stale commit=False (retry, never held lock)
B retry commit=True value=20 ver=2
HOT-ROW: counter sharded 4x, aggregate on read -> PASS
PASS
```

Version mismatch retries safely; no lock held across network calls; hot
rows shard instead of hammering one counter.
