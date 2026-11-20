# ailv-ui-chart-twin — worked example

Input: 5 raw sales rows (Mon 12, Mon 8, Tue 15, Tue 5, Wed 9).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: server rollup only (3 rows from 5 raw)
PASS: table under every chart
PASS: declarative JSON spec (Vega-Lite style)
PASS: stocked library, no hand-drawn SVG
PASS: twin readable at 360px (no sideways scroll)
twin table: [{"day": "Mon", "sales": 20}, {"day": "Tue", "sales": 20}, {"day": "Wed", "sales": 9}]
demo twin shipped -> twin-ok
```
