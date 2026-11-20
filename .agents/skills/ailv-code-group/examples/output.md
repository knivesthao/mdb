# ailv-code-group — worked example

## Input

Demo file list baked into `scripts/helper.py`: three `checkout/*` feature
files plus layer-scattered `models/user.py` and `controllers/user.py`.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
PASS grouped :: checkout/checkout_routes.py
PASS grouped :: checkout/checkout_models.py
PASS grouped :: checkout/checkout_tests.py
FAIL scattered by layer :: models/user.py (move next to feature)
FAIL scattered by layer :: controllers/user.py (move next to feature)
shared contracts: contracts.py
rule: follow the existing pattern over rewrites
```
