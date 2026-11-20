# ailv-code-crypto — worked example

## Input

Demo lines baked into `scripts/helper.py`: a hand-rolled XOR cipher,
a hardcoded `sk-live` key, a `secrets.token_urlsafe` call, and a bcrypt hash.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
line 1: hand-rolled cipher
line 2: possible secret in code
token issued: 2026-11-08T22:59:08+00:00
token expires: 2026-11-08T23:59:08+00:00 (scoped: read-only)
rule: platform crypto only; secrets in env; tokens expire and are scoped
```

(Timestamps reflect the run clock; the expiry is always issued + 1 hour.)
