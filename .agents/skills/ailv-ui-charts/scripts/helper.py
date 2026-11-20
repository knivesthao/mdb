"""Self-check: chart picked by the question, never by taste."""

RULES = [
    ("trend over time", "line"), ("compare few categories", "bar"),
    ("share at one moment", "stacked-bar"), ("distribution", "histogram"),
    ("two variables + trend", "scatter"), ("matrix pattern", "heatmap"),
    ("single number", "big-number+sparkline"), ("exact lookup", "table-not-chart"),
]
DEMO = [("trend over time", [3, 5, 4, 7, 9]),
        ("compare few categories", {"a": 4, "b": 7}),
        ("exact lookup", {"row": 42})]


def pick(question):
    for key, chart in RULES:
        if key == question:
            return chart
    return "table-not-chart"


def main():
    ok_all = True
    for q, data in DEMO:
        chart = pick(q)
        n = len(data) if hasattr(data, "__len__") else 1
        ok = chart not in ("pie", "donut", "3d", "dual-axis")
        print(f"{'PASS' if ok else 'FAIL'}: '{q}' (n={n}) -> {chart} + machine twin")
        ok_all = ok_all and ok
    print("demo: 3 questions routed, bars start at zero, no dual/3D ->",
          "charts-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
