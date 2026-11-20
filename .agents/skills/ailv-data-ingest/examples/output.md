# ailv-data-ingest — worked example

Input: 4 demo events — `evt-1` sent twice (retry), `evt-2` with an
additive `note` field, `evt-3` missing `amount_cents` (poison).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
DEDUP skip key=evt-1 (retry converged)
ADDITIVE pass-through key=evt-2 extra=['note']
POISON key=evt-3 missing=['amount_cents'] -> DLQ
STORE rows=2 dlq=1 dedup_keys=2
PASS
```

Retries converge (2 stored rows, no double-count), poison lands in the
DLQ, the stream never blocks, dedup store is TTL-bounded.
