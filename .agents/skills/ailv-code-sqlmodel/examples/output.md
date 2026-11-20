# ailv-code-sqlmodel — worked example

## Input

Stack mentions SQLModel; rules baked into `scripts/helper.py`.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
stack=sqlmodel -> order_by ignore-first
stack=sqlmodel -> no init validation asserts
stack=sqlmodel -> model_validate dict tests
stack=other     -> skip entirely when the stack has no SQLModel

rules: 3, gated, never default
```
