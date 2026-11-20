# ailv-code-integrity — worked example

## Input

Demo webhook payload baked into `scripts/helper.py`:
`{"event":"deploy","sha":"abc123"}` signed with HMAC-SHA256.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
payload: {"event":"deploy","sha":"abc123"}
signature: 1326410ddf431ae4...
verify good: True
verify tampered: False
PASS lockfiles committed
PASS webhook signatures verified
PASS no curl-to-shell installs
PASS bytes changed without commit -> stop and ask
```
