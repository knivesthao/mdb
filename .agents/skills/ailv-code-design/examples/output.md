# ailv-code-design — worked example

## Input

Demo feature baked into `scripts/helper.py`: avatar upload with abuse
story "10GB uploads looped", checked against the 5-item self-check.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
feature: avatar upload
who pays: us (storage+bw); who is hurt: viewers of forged images
abuse: 10GB uploads looped
PASS abuse story written per feature
PASS default deny, least privilege
PASS costly endpoints rate-limited
FAIL upload size capped
PASS response size capped
result: 4/5 checks pass
```
