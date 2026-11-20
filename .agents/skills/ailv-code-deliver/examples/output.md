# ailv-code-deliver — worked example

Input (demo, baked into `scripts/helper.py`): a bug-fix handover
(artifact `tests/test_quota.py + fix in quotas.py`, repro + before/after
proof, no screens changed, open edge tracked in #42).

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
PASS  handover names proof artifact, not process
PASS  sample outputs included
PASS  screenshots present iff screens changed
PASS  unresolved listed plainly
artifact: tests/test_quota.py + fix in quotas.py
proof: repro steps + before/after + guard test run
SELF-CHECK: PASS
```

Reading: the handover names its proof artifact instead of the process,
carries samples, skips screenshots only because no screen changed, and
lists the unresolved edge plainly. Exit code 0.
