# ailv-code-fallback — worked example

Input (demo, baked into `scripts/helper.py`): four features ranked by
criticality (checkout=core, order history=standard,
recommendations + polling/beacons=shed-first), stressed at peak x1/x2/x4.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
-- peak x1 --
  checkout: serve (on, no deploy)
  order history: serve (on, no deploy)
  recommendations: serve (on, no deploy)
  polling/beacons: serve (on, no deploy)
-- peak x2 --
  checkout: serve (on, no deploy)
  order history: serve-stale-cache (flag-gated, no deploy)
  recommendations: 429+Retry-After (flag-gated, no deploy)
  polling/beacons: 429+Retry-After (flag-gated, no deploy)
-- peak x4 --
  checkout: serve (on, no deploy)
  order history: serve-stale-cache (flag-gated, no deploy)
  recommendations: 429+Retry-After (flag-gated, no deploy)
  polling/beacons: 429+Retry-After (flag-gated, no deploy)
stress x4: core=serve, extras shed -> degraded mode holds
```

Reading: at x2+ the sheddable tiers drop behind flag gates (no deploy)
while core keeps serving — the stress test proves the degraded mode.
Exit code 0.
