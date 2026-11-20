# ailv-sec-waf — worked example

Input: demo requests vs rules baked into `scripts/helper.py`, run from
inside the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
waf mode: blocking
[PASS] blocking mode (monitor-only is decoration)
  [PASS] allowed legit: GET /search?q=hello+world
  [PASS] allowed legit: GET /item?id=42
  [PASS] BLOCKED (sqli): GET /x?q=' OR '1'='1
  [PASS] BLOCKED (xss): POST /comment body=<script>alert(1)</script>
  [PASS] BLOCKED (traversal): GET /file?p=../../etc/passwd
  [PASS] allowed legit: POST /checkout qty=2
demo: 3 attacks blocked, 0 missed, 0 false positives
[PASS] false positives tuned weekly (2 last week)
[PASS] sensitive traffic logged (no exemptions)
self-check: PASS
```

Reading it: blocking mode on, 3 attacks blocked, legit traffic untouched,
false positives tuned weekly. Exit code 0.
