# ailv-code-ssrf — worked example

## Input

Demo URLs baked into `scripts/helper.py` with allowlist
`{api.example.com, cdn.example.com}` and blocked internal hosts.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
ALLOW :: https://api.example.com/data
BLOCK not allowlisted :: https://evil.example.net/steal
BLOCK internal/metadata :: http://169.254.169.254/latest/meta-data/
ALLOW :: https://cdn.example.com/img.png
rule: timeouts + size caps on; prefer webhooks over server fetch
```
