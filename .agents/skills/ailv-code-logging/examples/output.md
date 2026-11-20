# ailv-code-logging — worked example

## Input

Demo security events baked into `scripts/helper.py`: failed login,
validation failure, permission denial, and a costly-endpoint spike.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
{"event": "login_failed", "reason": "bad password", "when": "2026-01-01T00:00:00Z", "who": "bob"}
{"event": "validation_failed", "field": "age", "reason": "negative", "who": "anon"}
{"action": "delete", "event": "permission_denied", "who": "bob"}
{"endpoint": "/api/report", "event": "costly_spike", "rpm": 900}
redaction demo: login with password=*** ok
rule: auth+deny events logged; no secrets; alerts on spikes
```
