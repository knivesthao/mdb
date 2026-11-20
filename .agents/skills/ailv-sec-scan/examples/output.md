# ailv-sec-scan — worked example

Input: demo image/dep inventory baked into `scripts/helper.py`, run from
inside the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
image/dep scan (demo):
  image app:1.4.2: pinned=True critical=0 high=2 rebuilt=6d ago
  image worker:latest: pinned=False critical=1 high=4 rebuilt=90d ago
  dep libauth 2.3.1: pinned=True critical=0
  dep libparse >=1.0: pinned=False critical=1
  warn: worker:latest: floating tag -> pin it
  warn: worker:latest: stale rebuild (90d) -> rebuild on schedule
  warn: libparse: unpinned range >=1.0
  BLOCK: worker:latest: 1 critical CVEs
  BLOCK: libparse: 1 critical CVEs
verdict: FAIL - build blocked on critical findings
```

Reading it: critical findings block the build, floating tags and stale
rebuilds flagged, scanner errors fail closed. Exit code 0.
