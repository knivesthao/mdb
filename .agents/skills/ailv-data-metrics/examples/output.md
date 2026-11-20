# ailv-data-metrics — worked example

Input: registry defines `revenue`; a duplicate name with a different
formula arrives; `orders` is defined; `revenue` changes to v2.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
READ revenue = sum(amount_cents) (dashboards never re-derive)
INCIDENT duplicate metric revenue: 'sum(amount_cents)' vs 'sum(amount)'
DEFINE orders -> PASS
CHANGE revenue v2 logged, history replayed -> PASS
PASS
```

One definition per metric; duplicates flag as incidents; changes version.
