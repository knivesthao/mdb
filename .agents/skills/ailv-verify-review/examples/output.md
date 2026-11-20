# ailv-verify-review — worked example

Input: demo diff hunks baked into `scripts/helper.py` (2 hunks in
app.py, one clean, one renamed to house style; fires once).

Run: `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
app.py:42 issue=none fix=n/a
app.py:55 issue=renamed helper to house style fix=applied
PASS: diff read before verdict, never memory
PASS: matched skills re-read, their checks hold
PASS: no dead code or debug leftovers
PASS: outputs agent-first, verdicts human-only
PASS: fires once per task; user can re-invoke any time
PASS: scope is the diff only, never the whole file
RESULT: PASS
```

Exit code 0. Scope is the diff only; fixes from this pass never re-trigger.
