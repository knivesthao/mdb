# ailv-data-quality — worked example

Input: a good batch (fresh, 20 rows, stable mean) and a bad batch
(nulls + distribution shift) against a prior mean of 100.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
GOOD fails=[] -> PASS promote
BAD fails=['nulls=3', 'distribution-shift mean=69999 prev=100'] -> BLOCKED page owner + sample attached
ROW-COUNT-ONLY would pass bad batch: volume=10 -> signals win -> PASS
PASS
```

Multi-signal gates block the bad batch; row counts alone would pass it.
