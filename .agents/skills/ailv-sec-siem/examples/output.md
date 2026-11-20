# ailv-sec-siem — worked example

Input: demo auth/admin/data-access events baked into `scripts/helper.py`,
run from inside the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
ingested 4 events (auth/admin/data-access) into hash-chained store
  [PASS] 2026-11-08T09:00:00Z auth: login ok ada chain=2dd56a9d9d7dd016
  [PASS] 2026-11-08T09:01:12Z admin: role grant bob chain=14b51464a44ff7a5
  [PASS] 2026-11-08T09:02:40Z data-access: export customers.csv chain=3153229a167d1003
  [PASS] 2026-11-08T09:03:55Z auth: login fail eve x14 chain=30f3c8403ff2d0a2
integrity verification: PASS (tested, not assumed)
[PASS] alert volume 1/day vs capacity 20/day: tuned
self-check: PASS
```

Reading it: tamper-evident hash chain verified (not assumed), alert volume
within analyst capacity. Exit code 0.
