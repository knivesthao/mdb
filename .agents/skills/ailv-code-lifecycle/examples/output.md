# ailv-code-lifecycle — worked example

Input (demo, baked into `scripts/helper.py`): four contract changes to
classify (remove, rename, add, typo fix) plus a two-skill install pack
run twice.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
PASS  'remove skill ailv-x' -> major
PASS  'rename event field' -> major
PASS  'add skill ailv-y' -> minor
PASS  'fix typo in docs' -> patch
install run1: (['skill-a', 'skill-b'], []) receipt: 2 landed
install run2: ([], []) (idempotent, marker skipped)
version endpoint: agent stops when equal -> equal, stop
ALL: PASS
```

Reading: the version bump matches the contract change, installs are
idempotent from the marker file (re-runs never duplicate), receipts say
what landed, and the update loop stops when the version is equal. Exit
code 0.
