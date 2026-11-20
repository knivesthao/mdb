# ailv-sec-patch — worked example

Input: demo fleet inventory baked into `scripts/helper.py`, run from inside
the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
patch window: 14d, baseline: CIS
[PASS] web-01: patched (5d), agent ok, no exemption
[PASS] db-01: patched (12d), agent ok, no exemption
[FAIL] exec-laptop: EXEMPT -> persistent foothold, include it; straggler (120d > 14d) -> page ops; no agent -> unmanaged
[FAIL] legacy-pos: EXEMPT -> persistent foothold, include it; straggler (200d > 14d) -> page retail
self-check: FAIL (2 hosts need attention)
```

Reading it: no exemptions honored — exec and legacy stragglers flagged and
their owners paged; measured 14-day window. Exit code 0.
