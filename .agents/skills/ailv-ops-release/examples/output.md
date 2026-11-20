# ailv-ops-release — worked example

Input: current version `1.4.2`, change kind `minor` (new skill added),
4 finished changes batched, 0 releases cut today.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: batched: one version for 4 changes
PASS: semver bump 1.4.2 -> 1.5.0 (minor)
PASS: changelog, signatures, feed, version move together
PASS: no second release today (or hotfix only)
release: 1.5.0 (changes: 4)
  - add preview auto-stop
  - fix probe timeout
  - docs touch-up
  - refactor helper
```

Exit code: 0. One version (1.5.0) for the whole batch.
