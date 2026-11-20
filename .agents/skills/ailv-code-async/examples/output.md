# ailv-code-async — worked example

Input (demo, baked into `scripts/helper.py`): two slow jobs submitted
to a queue (`resize-img`, `send-receipt` which fails once), worker pool
of 2, partial-ship failure policy.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
submitted -> ['job-1', 'job-2'] (request not held open)
fan-out pool size: 2 (bounded); failure policy: partial ship + retry
job-1: done after 1 tries; notify on completion
job-2: attempt 1 failed -> retry (idempotent)
job-2: done after 2 tries; notify on completion
stall SLA: 5m watchdog, silent dead worker pages
```

Reading: the request returns job ids immediately, fan-out stays
bounded, the failed job retries safely (idempotent) with a stall SLA
watching for silent dead workers. Exit code 0.
