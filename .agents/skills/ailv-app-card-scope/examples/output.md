# Example: card scope self-check

Input: 3 demo log lines scanned for card-like patterns, run with `python3 scripts/helper.py`.

Actual output:

```
PASS: log line clean: 'INFO checkout session created id=cs_123'
PASS: log line clean: 'INFO refund issued via provider api pi_456'
PASS: log line clean: 'DEBUG card ending 4242 approved'
PASS: card entry in provider iframes; SAQ A current
PASS: refunds run through provider API
RESULT: PASS
```

No card numbers in logs; exit 0.
