# ailv-data-model — worked example

Input: a canonical flat record (units in names, ISO-8601 UTC, explicit
status) and a bad record (abbrev `amt`, 4-deep nesting, no status,
non-ISO time).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
GOOD fails=[] -> PASS
BAD fails=['nested-too-deep', 'tribal-abbrev: amt -> amount_cents', 'null-means-something: use explicit status', 'time-not-iso8601'] -> PASS blocked
PASS
```

One canonical shape per concept; nesting capped, no clever nulls.
