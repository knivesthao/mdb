# ailv-ui-charts — worked example

Input: three questions — trend over time (5 pts), compare few categories (2), exact lookup.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: 'trend over time' (n=5) -> line + machine twin
PASS: 'compare few categories' (n=2) -> bar + machine twin
PASS: 'exact lookup' (n=1) -> table-not-chart + machine twin
demo: 3 questions routed, bars start at zero, no dual/3D -> charts-ok
```
