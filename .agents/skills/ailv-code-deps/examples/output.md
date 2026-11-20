# ailv-code-deps — worked example

## Input

Demo requirements baked into `scripts/helper.py`: two pinned entries,
two unpinned entries, and one vendored copy.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
PASS pinned :: fastapi==0.115.0
PASS pinned :: pydantic==2.9.2
FAIL unpinned :: requests>=2.0
FAIL unpinned :: typer
FAIL never vendor a copy you will forget to patch :: sqlmodel==0.0.22  # vendored copy in ./vendor
audit: pip audit (scheduled); unused deps removed
```
