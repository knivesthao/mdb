# ailv-code-billing — worked example

Input (demo, baked into `scripts/helper.py`): plan versions
`pro-2025-q1=2000c`, `pro-2025-q3=2500c`; one idempotent subscribe
(customer acme + plan + key `idem-1`, retried once); two metered events.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
idempotent subscribe: sub_1 == sub_1 -> PASS
event @ pro-2025-q1: charge 2000c
event @ pro-2025-q3: charge 2500c
entitlement: only on verified webhook (sig ok) -> entitled
failed payment: remind -> retry -> grace (no instant cancel)
```

Reading: the retry converges on one subscription, each charge resolves
from the plan in effect when the event landed (never hardcoded),
entitlement waits for the verified webhook, and failed payments dunning
before any cancel. Exit code 0.
