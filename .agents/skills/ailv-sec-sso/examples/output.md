# ailv-sec-sso — worked example

Input: demo users + exceptions baked into `scripts/helper.py`, run from
inside the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
identity provider: idp-primary (single)
[PASS] ada: ok
[PASS] bob: jit-provisioned, domain verified
[FAIL] legacy-svc: not on single IdP / legacy password-only login
[FAIL] ex-admin: still provisioned after IdP removal -> deprovision now
[PASS] break-glass-1: expires 2026-12-01, owned, audited
[FAIL] vendor-temp: exception without owner
self-check: FAIL (3 items need attention)
```

Reading it: single IdP enforced, JIT provisioning verified, legacy login and
stale account flagged, break-glass exception owned/expiring/audited. Exit
code 0.
