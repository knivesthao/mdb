# ailv-ops-safety — worked example

Input: agent scoped to its own area (`svc/api-deploy`, `svc/api-data`,
nothing from the never-touch list); destructive op `drop table users`
without human approval stays unexecuted; fail streak 0; spend $120/$500
with kill switch armed.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: agents scoped least-privilege, never-touch enforced
PASS: destructive ops wait for human approval first
PASS: no agent approver / no emergency bypass
PASS: failing actors auto-drained (streak 0)
PASS: spend capped with alerts + kill switch
safety: scope=['svc/api-data', 'svc/api-deploy'] spent $120/$500 drain=False
```

Exit code: 0. Blast radius contained, destructive op blocked.
