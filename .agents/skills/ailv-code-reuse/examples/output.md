# ailv-code-reuse — worked example

## Input

Demo file set baked into `scripts/helper.py`: the same Pay button markup
in `checkout.py` and `refund.py`, one Avatar use in `profile.py`.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
DUPLICATE x2 -> use ui/buttons.py:PayButton
single use ok :: <avatar size='sm'/>
rule: repo first, then stack library; third copy never pasted
```
