# ailv-verify-benchmark — worked example

Input: demo trial table baked into `scripts/helper.py` (3 lanes:
matched-skills / whole-bank / no-skills, one real task, plan rules kept).

Run: `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
demo method: real task, plan rules kept (inline<=5 steps else file), 1 run per lane
raw numbers: [{"label": "matched-skills", "tokens": 4200, "seconds": 61.0, "defects": 1}, {"label": "whole-bank", "tokens": 6100, "seconds": 88.0, "defects": 1}, {"label": "no-skills", "tokens": 5900, "seconds": 74.0, "defects": 3}]
PASS: with/without/no-skill trial run
PASS: tokens, time, defects all reported
PASS: method plus raw numbers published
best lane: matched-skills (tokens=4200, time=61s, defects=1)
RESULT: PASS
```

Exit code 0. Method plus raw numbers are printed with the result.
