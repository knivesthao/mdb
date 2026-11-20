# ailv-ops-index — worked example

Input: 4 routing queries (migration, stuck canary rollout, db password
rotation, PR preview env) against the 14-skill ops map.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: 'migration' -> ailv-ops-migrate
PASS: 'canary rollout is stuck' -> ailv-ops-rollout
PASS: 'rotate the db password' -> ailv-ops-secrets
PASS: 'preview env for my PR' -> ailv-ops-preview
PASS: index covers 14 ops skills (14)
index verdict: ONLY-MATCHED-READ
```

Exit code: 0. Each task routes to exactly its owning skill.
