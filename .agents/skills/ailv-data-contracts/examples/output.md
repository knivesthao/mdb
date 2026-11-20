# ailv-data-contracts — worked example

Input: registry holds `order.v1`; candidate `order.v2` adds optional
`note`; a second candidate renames `order_id` to `id`.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
ADDITIVE order.v2 fields=['amount_cents', 'note', 'order_id'] -> PASS
RENAME order.v2 fields=['amount_cents', 'id'] removed=['order_id'] -> BLOCKED new version required
CONSUMER pins order.v1; producer dual-writes v1+v2 -> PASS
PASS
```

Additive change passes; the rename is blocked pending a new version.
