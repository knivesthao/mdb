# ailv-verify-layout — worked example

Input: demo viewport measurements baked into `scripts/helper.py`
(320px + desktop, zero horizontal scroll, aligned baselines/edges,
exempt data table inside a stocked component).

Run: `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
viewport 320px: h_scroll=0 chopped=none baseline=True edges=True
viewport 1280px: h_scroll=0 chopped=none baseline=True edges=True
exempt: data table scrolls only inside stocked component (allowed)
PASS: no loss or 2D scroll at 320px (WCAG 1.4.10)
PASS: rows share baselines, columns share edges
PASS: 2D scroll only in stocked components for exempt content
RESULT: PASS
```

Exit code 0. A purposely dense user-ordered design would ship with a flag.
