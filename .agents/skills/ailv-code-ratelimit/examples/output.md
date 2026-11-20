# ailv-code-ratelimit — worked example

## Input

Demo traffic baked into `scripts/helper.py`: 130 requests from one client
against a 120-requests-per-60s sliding window.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
allowed: 120 of 130 (limit 120/min)
blocked: 10 (counted separately)
over-limit -> 429 with Retry-After: 60
ok, retry_after=60, remaining=0
rule: limits in config; caps on size/complexity/page/spend
```
