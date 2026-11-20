# ailv-code-token — worked example

## Input

Demo snippet baked into `scripts/helper.py` with three functions:
`route` (table-driven), `unused_helper` (dead), `nested` (depth 3).

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
functions: nested, route, unused_helper
dead exports: unused_helper
depth route: 1
depth unused_helper: 0
depth nested: 3
rule: nesting>2 fails; dead code deleted; one pattern per job
```
