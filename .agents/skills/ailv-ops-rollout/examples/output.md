# ailv-ops-rollout — worked example

Input: canary at 5% traffic (err 0.6%, p95 200ms) vs baseline
(err 0.4%, p95 180ms); predefined rollback trigger, one-action rollback
to v1.4.2, stateless service, no 100%-at-once burst.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: progressive steps with health gates (canary 5%)
PASS: canary compared to baseline before promote
PASS: rollback trigger predefined
PASS: rollback is one action, restores last good in minutes
PASS: stateless rolls back; stateful rolls forward
PASS: no 100%-at-once outside declared emergency
PASS: halt rules evaluated (halt=False)
canary err 0.6% vs baseline 0.4% (delta +0.2pt)
canary p95 200ms vs baseline 180ms (+11.1%)
rollout verdict: PROMOTE
```

Exit code: 0. Deltas (+0.2pt err, +11.1% p95) under halt thresholds.
