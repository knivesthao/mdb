# ailv-ops-preview — worked example

Input: PR #117 (merged), preview env mirroring prod with seeded demo data
(no prod dump), URL posted to the PR, destroyed on merge, idle 75min
against a 60min timeout with auto-stop fired.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: per-PR prod mirror
PASS: seeded demo data, never prod dumps
PASS: preview URL posted back to PR
PASS: destroyed on merge
PASS: idle auto-stop fires
preview env for PR #117: STOPPED
preview url: https://pr-117.preview.example (posted: True)
```

Exit code: 0. No straggler env, no prod data leaked.
