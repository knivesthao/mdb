---
name: ailv-app-card-scope
description: "One logged card number turns a SAQ A checkout into a breach."
sources:
  - title: PCI Security Standards Council
    url: https://www.pcisecuritystandards.org/
  - title: Stripe Elements
    url: https://docs.stripe.com/payments/elements
helper: scripts/helper.py
example: examples/output.md
---

# Keep card scope at SAQ A

`ailv-app-card-scope` (Keep card scope at SAQ A): Keep card entry inside the provider's iframes (Checkout, Elements) so the merchant qualifies for SAQ A; complete the SAQ annually and reconfirm embedded-form eligibility in the provider dashboard. Card numbers never touch our servers, logs, databases, or emails — assert it with a test that fails on card-like patterns, never assume it. Never log full card numbers even while debugging; truncate or drop them at the edge. Refunds and voids run through the provider API, never by replaying card details.

## Checks

- card entry stays in provider iframes; SAQ A current
- no card numbers in servers, logs, databases, or emails
- card-like-pattern test guards every new log line
- refunds run through the provider API
