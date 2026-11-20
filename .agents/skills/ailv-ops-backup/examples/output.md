# ailv-ops-backup — worked example

Input: backup every 30min against a 60min RPO; last drill restored in
95min against a 120min RTO, recorded, into an isolated env (never over
prod), erasure log replayed first.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: schedule matched to RPO (30min <= RPO 60min)
PASS: restore drilled, timed against RTO (95min <= RTO 120min)
PASS: drill result recorded
PASS: restore tested isolated, never over prod
PASS: erasure log replayed before opening restore
backup: every 30min (RPO 60min); last drill restore 95min (RTO 120min)
```

Exit code: 0. Tested backup inside both RPO and RTO.
