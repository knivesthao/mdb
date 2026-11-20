# ailv-ops-coordinate — worked example

Input: shared plan ledger where `deploy-api` is live-leased to agent-A
(area `svc/api`); agent-B (area `svc/web`) tries to claim it, then claims
free task `deploy-web` and completes it with a structured status record.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: one shared plan ledger, tasks claimed before start
PASS: live lease rejects second claim with 409
PASS: no work on held task (rejection honored)
PASS: one feature dir per agent, no overlap
PASS: cross-area edits need plan note first
PASS: idempotent steps converge on retry
PASS: status as structured records, not prose
PASS: scoped credentials: own area only
ledger: deploy-api held by agent-A (claim->409), deploy-web claimed+done by agent-B
```

Exit code: 0. Held task rejected with 409 and left alone.
