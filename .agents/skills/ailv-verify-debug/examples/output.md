# ailv-verify-debug — worked example

Input: demo 4-step plan baked into `scripts/helper.py`; smallest input
`qty=-1` (was order #1042 with 37 lines) still fails at "render total".

Run: `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
smallest failing input: qty=-1 (was order #1042 with 37 lines)
guilty step: render total
contract fix: render total now honors fetch record's cents-int contract
PASS: smallest failing input reproduced
PASS: guilty step bisected by done-state
PASS: contract fixed when steps disagree
RESULT: PASS
```

Exit code 0. Guilty step is the first whose output fails its done-state check.
