# ailv-verify-tests — worked example

Input: demo case list baked into `scripts/helper.py` (happy path +
one edge), single command `pytest -q`.

Run: `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
command: pytest -q
PASS: happy path: valid checkout
PASS: edge: empty cart rejected
PASS: one command runs all checks
PASS: edge case covered
PASS: output is parseable
RESULT: PASS
```

Exit code 0. One command, edge covered, lines parse as PASS/FAIL.
