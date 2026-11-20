# ailv-code-language — worked example

## Input

Demo dicts baked into `scripts/helper.py`: a valid user
`{"name": "Ada", "age": 30}` and an invalid user `{"name": " ", "age": -1}`.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
valid input -> CreateUser(name='Ada', age=30)
invalid input -> user=None error=name must be a non-empty string
rule: one typed model drives validation; no hand-written type checks per field
```
