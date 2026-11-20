# ailv-data-lineage — worked example

Input: run records `orders-db -> marts.orders -> dash.revenue`;
trace `dash.revenue` to its origin.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
RUN r1: orders-db --[normalize]--> marts.orders
RUN r2: marts.orders --[revenue_sum]--> dash.revenue
ORIGIN dash.revenue = orders-db (one lookup)
PASS
```

Run-time records trace any number to its origin in one lookup.
