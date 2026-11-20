# ailv-code-plan — worked example

Input (demo, baked into `scripts/helper.py`): 4 matched leaves
(billing, rbac, notify + cleanup), 2 unblocked, all fetched up front.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
PASS  plan written (3+ matched leaves)
PASS  inline plan ok (<=5 steps, live session)
PASS  every step names skill + done-state
PASS  independents run together (2 unblocked)
PASS  all skills fetched once up front, none during exec
PASS  last step is cleanup
PASS  tree holds only deliverable + tests
SELF-CHECK: PASS
```

Reading: the demo plan satisfies every Checks line of the skill —
numbered steps with done-states, independents in parallel, one batched
fetch, cleanup last. Exit code 0.
