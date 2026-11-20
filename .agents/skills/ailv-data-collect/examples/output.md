# ailv-data-collect — worked example

Input (demo, baked into `scripts/helper.py`): a file source of 4 events
with `(updated_at, id)` ordering; two polls, the first with a retried
duplicate delivery.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
push-capable sources: webhooks in (not polled); polling this file source
poll 1: fetched 4, landed 4 (dupes dropped)
poll 2: fetched 0, landed 0 (dupes dropped)
restart resumes from cursor (3, 4) (no re-read, no skip)
converged at landing: [1, 2, 3, 4]
```

Reading: push-capable sources use webhooks, the poll-only source is read
through an ordered cursor so restarts resume exactly, and at-least-once
retries converge via dedup at the landing. Exit code 0.
