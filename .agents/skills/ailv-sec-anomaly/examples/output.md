# ailv-sec-anomaly — worked example

Input: demo login events baked into `scripts/helper.py`, run from inside
the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
baseline retuned 6d ago [PASS] (continuous retuning)
  [queue] ada from SG: normal -> analyst review
  [queue] bob from SG: normal -> analyst review
  [PAGE] eve SG->BR: impossible-travel
  [PAGE] svc LAN->LAN: lateral-movement
  [queue] ada from SG: normal -> analyst review
demo: 2 paged (sharp only), 3 queued for review
[PASS] only sharp signals page; rest stays in review queue
self-check: PASS
```

Reading it: baseline freshly retuned, only impossible-travel and
lateral-movement page; normals stay in the review queue. Exit code 0.
