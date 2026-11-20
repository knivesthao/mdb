# ailv-code-notify — worked example

Input (demo, baked into `scripts/helper.py`): queue an order-paid
receipt for carol (quiet hours on) plus its retry, one for dave (quiet
off), and a promo for unsubscribed mallory.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
queued
queued (retry)
queued
suppressed: unsubscribed (marketing path separate)
  order-7:paid -> carol: digested batch ['email']: Order 7 paid.
  order-7:paid -> carol: deduped (already sent)
  order-8:paid -> dave: send ['email', 'push']: Order 8 paid.
provider caps absorbed by queue; transactional/marketing paths split
```

Reading: sends go through the queue with templates (never blocking),
the retried event key dedups instead of double-notifying, quiet hours
digest into a batch, and the unsubscribed user is suppressed. Exit
code 0.
