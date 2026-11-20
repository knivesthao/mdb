# ailv-verify-scope — worked example

Input: demo change list baked into `scripts/helper.py` (copy fix ->
fast lane; webhook verify -> full suite; unsure flag -> full suite).

Run: `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
copy fix on checkout button [words] -> fast suite
webhook signature verify [behavior] -> full suite
unsure: new env flag [doubt] -> full suite
PASS: behavior changes earn the full suite once
PASS: words and styling earn syntax plus smoke
PASS: fast path never skips the ship gate
PASS: doubt runs the full suite
RESULT: PASS
```

Exit code 0. Doubt runs the full suite; the fast path never skips the gate.
