# ailv-ops-pipeline — worked example

Input: demo deploy run through the shared template `shared/deploy.yml`
(commit `abc1234`): gates build/tests/security-scan/plan-preview/approval,
one medium scan finding (ticketed T-42), a machine-readable mutating plan,
one-action rollback to artifact v1.4.2, start/finish trigger events.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: one shared template, no hand-rolled pipes
PASS: gates in order all green
PASS: mutating step publishes machine-readable plan
PASS: rollback is one action on old artifact
PASS: no critical scan findings blocking
PASS: deploy start/finish events emitted
PASS: preview env auto-stops
PASS: deploy links to commit
pipeline verdict: SHIP
{
  "template": "shared/deploy.yml",
  "commit": "abc1234",
  "rollback": {
    "action": "redeploy",
    "artifact": "v1.4.2",
    "steps": 1
  }
}
```

Exit code: 0. Verdict SHIP: every check in SKILL.md holds.
