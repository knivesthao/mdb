# ailv-code-track — worked example

## Input

Demo actions baked into `scripts/helper.py`: `used`, `copied`, `failed`,
and `slow` events plus one rejected identity-carrying event.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
emit: {"action": "used", "feature": "search"}
emit: {"action": "copied", "feature": "snippet"}
emit: {"action": "failed", "feature": "checkout"}
emit: {"action": "slow", "feature": "report"}
blocked: identity in event: email
sink today: /tmp/ailv-track-demo.jsonl (swap to warehouse without touching callers)
```
