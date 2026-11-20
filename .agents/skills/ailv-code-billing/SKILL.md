---
name: ailv-code-billing
description: "Billing bugs refund money or lock out paying users — both fail loudly and publicly."
sources:
  - title: Stripe Billing
    url: https://docs.stripe.com/billing
  - title: Stripe webhooks
    url: https://docs.stripe.com/webhooks
helper: scripts/helper.py
example: examples/output.md
---

# Bill from plans, never hardcode

`ailv-code-billing` (Bill from plans, never hardcode): Bill from plan versions, never hardcoded amounts: every charge resolves price from the plan in effect when the metered event landed. Checkout sessions are idempotent — one customer plus plan plus idempotency key maps to one subscription. Fulfill and entitle only on signed provider webhooks, verified before trusting, with retry-safe handlers that converge on replay. Failed payments enter dunning (remind, retry, grace) before any cancel. Metered usage flows from ailv-code-track events, not from scattered counters. Prorate upgrades and downgrades at the switch, never at month end.

## Checks

- no hardcoded prices
- entitlement only on verified webhooks
- dunning before cancel
