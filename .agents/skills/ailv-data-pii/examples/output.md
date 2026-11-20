# ailv-data-pii — worked example

Input: scan `users-csv` (email hidden in `note`, phone in `phone_col`)
and a new webhook source with nothing labeled.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
PII email in ['note'] -> label at source
PII phone in ['phone_col'] -> label at source
RETENTION acts on labels -> PASS
NEW SOURCE labels=none -> QUARANTINE until classified
PASS
```

Scheduled scans label PII at the source; unlabeled sources quarantine.
