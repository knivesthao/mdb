---
name: ailv-app-tax
description: "Wrong-region tax is owed from the first sale, plus penalties."
sources:
  - title: Stripe Tax
    url: https://docs.stripe.com/tax
helper: scripts/helper.py
example: examples/output.md
---

# Charge tax where the buyer is

`ailv-app-tax` (Charge tax where the buyer is): Charge the right tax where the buyer is, not where the seller sits. Digital B2C sales into the EU need Non-Union OSS from the first sale; US states each set their own nexus thresholds; physical goods follow origin rules that differ again. Use provider tax automation or sell through a Merchant of Record, and flag the decision to the owner instead of improvising. Keep location-evidence records (two corroborating pieces per EU sale) for as long as the regime requires. Never hardcode a rate that the provider should resolve.

## Checks

- tax route chosen per buyer region, never improvised
- EU digital sales covered from the first sale
- location evidence kept per regime
- no hardcoded rates the provider should resolve
