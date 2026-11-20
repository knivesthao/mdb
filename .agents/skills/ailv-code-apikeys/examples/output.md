# ailv-code-apikeys — worked example

Input (demo, baked into `scripts/helper.py`): issue key `k1`
(scopes `[orders.read]`, rate limit 2) with demo secret `sk-live-ABC`,
then good / wrong-scope / over-rate / revoked calls.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
created k1, secret shown once: sk-live-ABC (stored: hash only)
good call: allow
wrong scope: deny: out of scope
rate 3rd call: allow / deny: rate exceeded
after revoke: deny: revoked/unknown
metered calls attributed to k1: 3
```

Reading: only the hash is stored, the secret is shown once, scope and
per-key rate limits are enforced, revocation is instant, and every call
is attributed to the key for metering. Exit code 0.
