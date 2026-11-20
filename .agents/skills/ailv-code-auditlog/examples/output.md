# ailv-code-auditlog — worked example

Input (demo, baked into `scripts/helper.py`): three events (permission
change, data export, impersonation start — each naming its agent) plus a
retention-window export.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
append-only rows: 3 (edits: none allowed)
export for auditors:
[
 {
  "actor": "agent:checkout-fix",
  "action": "members.write",
  "target": "ws=acme user=bob->admin",
  "day": 100
 },
 {
  "actor": "agent:checkout-fix",
  "action": "data.export",
  "target": "ws=acme orders.csv",
  "day": 101
 },
 {
  "actor": "ops:ada",
  "action": "impersonate.start",
  "target": "ws=globex consent=ticket-5",
  "day": 102
 }
]
retention 365d prunes 1 stale row -> kept 3
```

Reading: the trail is immutable actor-action-target events (the agent
is named in the actor field), the rows auditors ask for come first,
and export plus retention are built in. Exit code 0.
