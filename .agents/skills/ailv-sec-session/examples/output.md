# ailv-sec-session — worked example

Input: demo sessions baked into `scripts/helper.py`, run from inside the
skill folder:

```
python3 scripts/helper.py
```

Real output:

```
policy: access<=15m absolute<=480m rotation=True revocation=True
[PASS] sess-ada-1: age=10m -> PASS: live, short-lived, revocable
[FAIL] sess-bob-2: age=500m -> FAIL: past absolute cap -> kill
[PASS] sess-eve-3: age=5m -> DEAD (revoked server-side)
revocation kill-path: PASS
self-check: FAIL (1 sessions violate policy)
```

Reading it: short-lived with rotation enforced, absolute cap kills the stale
session, stolen session dies via server-side revocation. Exit code 0.
