---
name: ailv-ui-chart-twin
description: "Pixels convince humans but starve agents — the twin feeds both from one source."
sources:
  - title: Apache ECharts
    url: https://echarts.apache.org/
  - title: Vega-Lite
    url: https://vega.github.io/vega-lite/
helper: scripts/helper.py
example: examples/output.md
---

# Every chart ships its machine twin

`ailv-ui-chart-twin` (Every chart ships its machine twin): Aggregate on the server and ship only chart-ready rollups — never raw rows for the browser to group. Ship every chart with its machine twin: the data table underneath plus, when interactive, a declarative JSON spec in the Vega-Lite style — the agent judges and regenerates from table and spec, never from pixels. Encode by the measured ranking: position on a common scale beats length beats angle beats area beats color. Reach for a stocked chart library (Apache ECharts, Recharts) instead of hand-drawn SVG. The twin is the phone fallback: on narrow screens the table underneath carries what the shrunken chart can't — keep it complete and readable at 360px with no sideways page scroll.

## Checks

- chart-ready rollups only, no raw rows
- table plus spec under every chart
- stocked library, no hand-drawn SVG
- twin table complete and readable at 360px
