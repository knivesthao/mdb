# Example: legal mail self-check

Input: 2 demo mails (order receipt, sale newsletter) run with `python3 scripts/helper.py`.

Actual output:

```
INFO: order receipt kind=transactional consent=False opt_out=False
INFO: sale newsletter kind=marketing consent=True opt_out=True
PASS: order mail transactional-only, no marketing inside
PASS: marketing needs prior consent plus working opt-out
PASS: buyer lists never merged into marketing
PASS: suppression list kept indefinitely
RESULT: PASS
```

Transactional mail carries no marketing; exit 0.
