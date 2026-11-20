# ailv-code-flags — worked example

Input (demo, baked into `scripts/helper.py`): flag `new-checkout`
(owner billing-team, plans pro/team, 50% rollout, kill switch off) and
stale killed flag `old-banner`; four evaluations.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
PASS  new-checkout plan=pro bucket=10 -> on
PASS  new-checkout plan=pro bucket=90 -> off
PASS  new-checkout plan=free bucket=10 -> off
PASS  old-banner plan=pro bucket=0 -> off
owner(new-checkout)=billing-team, kill switch wired -> yes
stale flag past remove_by (old-banner) -> delete it
ALL: PASS
```

Reading: evaluation is targeted by plan + rollout percent (never a bare
boolean), the kill switch forces off, every flag has an owner, and the
stale flag past its removal date is deleted. Exit code 0.
