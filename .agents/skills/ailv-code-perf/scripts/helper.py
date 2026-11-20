"""ailv-code-perf helper: check demo measurements against budgets."""
import sys

BUDGETS = {"page_kb": 200, "endpoint_ms": 300, "queries_per_list": 1}

# Demo measurements: (name, metric, value)
MEASUREMENTS = [
    ("landing page weight", "page_kb", 142),
    ("GET /orders endpoint p95", "endpoint_ms", 210),
    ("order list query count (joined)", "queries_per_list", 1),
    ("search endpoint p95 (N+1 present)", "endpoint_ms", 1240),
]


def main():
    failures = 0
    for name, metric, value in MEASUREMENTS:
        budget = BUDGETS[metric]
        if metric == "queries_per_list" and value > 1:
            print(f"FAIL  {name}: {value} queries (N+1) > budget {budget} -> batch or join")
            failures += 1
        elif value <= budget:
            print(f"PASS  {name}: {value} <= budget {budget}")
        else:
            print(f"FAIL  {name}: {value} > budget {budget} -> shrink payload / cache / background it")
            failures += 1
    print(f"budgets checked: {len(MEASUREMENTS)}, over budget: {failures}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
