# ailv-ops-observe — worked example

Input: 2 demo alerts (checkout error rate, p99 latency climb), each with
request id, runbook link, owner, user-facing symptom, and a signed
schema-versioned trigger event; JSON health endpoint plus an independent
external probe.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: one id across logs, metrics, traces
PASS: every page actionable with runbook
PASS: every alert has an owner
PASS: alerts on user-facing symptoms only
PASS: alerts emitted as signed schema-versioned events
PASS: health exposed as JSON + deploy receipts
PASS: independent external check exists
observe verdict: 2/2 alerts healthy
{
  "alerts": 2,
  "health": {
    "endpoint": "/healthz",
    "format": "json",
    "receipt": "ok"
  }
}
```

Exit code: 0. All pages actionable, owned, and traceable.
