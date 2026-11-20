---
name: ailv-ui-charts
description: "A chart picked by taste misleads; a chart picked by the question reads itself."
sources:
  - title: Cleveland-McGill graphical perception
    url: https://doi.org/10.1080/01621459.1984.10478080
helper: scripts/helper.py
example: examples/output.md
---

# Which chart for which question

`ailv-ui-charts` (Which chart for which question): Pick the chart by the question, never by taste: trend over time goes line; comparison across a few categories goes bar; share of a whole at one moment goes stacked bar, share changing over time goes 100% stacked — pie only at five slices or fewer, never a donut for data; distribution goes histogram, five-number summaries go box plot; two variables go scatter with a trend line; matrix patterns go heatmap; a single number goes big text plus sparkline. Lookups go in a table, not a chart — charts show shapes, tables answer what-exactly. One message per chart: never dual axes, never 3D, never truncated bar axes — bars start at zero, log scale only across orders of magnitude. Label directly on the marks; the legend is the fallback. Small screens shrink the chart, never the message: simplify the marks, keep bars at zero, and let the machine twin carry the exact numbers a phone can't show. Then read ailv-ui-chart-twin and ship the chart's machine twin with it.

## Checks

- chart matches the question
- no dual axes, 3D, or truncated bars
- machine twin shipped per ailv-ui-chart-twin
- message intact at 360px, exact numbers in the twin
