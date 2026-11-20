# ailv-data-retain — worked example

Input: `events` aged 100d (policy 90d), `pii_profile` aged 40d (policy
30d), and a deletion request for subject `user-7`.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
EXPIRE dataset=events age=100d > 90d -> cold-store (open parquet)
EXPIRE dataset=pii_profile age=40d > 30d -> cold-store (open parquet)
DSR subject=user-7 key shredded -> proof=receipt-user-7 PASS
PASS
```

Expired data cold-stores in open formats; the subject key shred gives
deletion with proof.
