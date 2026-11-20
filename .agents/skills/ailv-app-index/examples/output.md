# ailv-app-index — worked example

Input (demo, baked into `scripts/helper.py`): five product requests
(billing, invites, search, legal, notify) routed to product skills.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
  billing -> ailv-code-billing
  invites -> ailv-code-invites
  search -> ailv-code-search
  legal -> ailv-app-legal
  notify -> ailv-code-notify
PASS  only matched product skills read
PASS  auth always via ailv-code-auth
PASS  new product work metered with ailv-code-track
SELF-CHECK: PASS
```

Reading: only the matched product skills are read (never the whole
shelf), login always routes to ailv-code-auth, and new product work is
metered with ailv-code-track. Exit code 0.
