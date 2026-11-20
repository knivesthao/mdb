# ailv-code-invites — worked example

Input (demo, baked into `scripts/helper.py`): issue a member invite for
workspace acme (accept twice to prove single-use), one already-expired
token, then owner removals down to the last owner.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
accept 1: grant member in acme to carol (logged)
accept 2 (reuse): deny: invalid/used/expired
expired: deny: invalid/used/expired
remove bob: removed
remove ada (last owner): blocked: workspace would be ownerless
```

Reading: tokens are single-use and expiring (reuse and expiry both
deny), acceptance grants exactly the invited role in the invited
workspace as a logged event, and the removal that would orphan the
workspace is blocked. Exit code 0.
