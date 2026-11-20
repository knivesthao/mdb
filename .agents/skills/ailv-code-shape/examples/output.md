# ailv-code-shape — worked example

## Input

Demo module baked into `scripts/helper.py`: `validate` (typed errors,
early returns) and `risky` (bare `except Exception`).

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
module lines: 12 (limit 150)
FAIL bare/except-Exception in risky: name exceptions
PASS typed errors at boundaries (ValueError with input attached)
PASS flat depth<=2 with early returns
rule: behavior lives next to what it acts on
```
