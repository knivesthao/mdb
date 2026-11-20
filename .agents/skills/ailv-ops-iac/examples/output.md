# ailv-ops-iac — worked example

Input: env defined in `git: infra/prod` (no click-ops), clean-account
reproducible; plan reviewed before apply; drift check every 15min with
paging; state locked and backed up; no current drift.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: version-controlled, reproducible from clean account
PASS: plan reviewed before apply on shared env
PASS: drift detection scheduled (15m)
PASS: drift pages when reality diverges
PASS: state locked and backed up like prod data
PASS: current drift: none
iac: git: infra/prod reproduces clean; state locked=True backed_up=True
```

Exit code: 0. Infra reproducible, drift watched, state safe.
