# ailv-code-search — worked example

Input (demo, baked into `scripts/helper.py`): three docs across two
tenants (acme owns "Refund policy" + "Referral program", globex owns a
far more popular "Refund policy"); queries `refund`, typo `refnd`, and
`zzz-no-match`.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
acme 'refund': ['Refund policy']
acme 'refnd' (typo): ['Refund policy']
acme 'refund' leaks globex doc: no leak
acme 'zzz-no-match': []
dead-search log (roadmap): [('acme', 'zzz-no-match')]
index maintained on writes (no nightly rebuild)
```

Reading: every query is tenant-scoped (globex's hotter doc never
leaks), results rank by relevance with typo tolerance, and the dead
search is logged as roadmap. Exit code 0.
