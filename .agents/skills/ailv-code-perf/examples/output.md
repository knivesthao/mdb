# ailv-code-perf — worked example

Input (demo, baked into `scripts/helper.py`): budgets
`{page_kb: 200, endpoint_ms: 300, queries_per_list: 1}` and four demo
measurements (page weight, two endpoint p95s, one list query count).

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
PASS  landing page weight: 142 <= budget 200
PASS  GET /orders endpoint p95: 210 <= budget 300
PASS  order list query count (joined): 1 <= budget 1
FAIL  search endpoint p95 (N+1 present): 1240 > budget 300 -> shrink payload / cache / background it
budgets checked: 4, over budget: 1
```

Reading: the search endpoint is over budget and shows an N+1 smell —
batch or join on an indexed column, cache the repeat work, re-measure.
Exit code 0.
