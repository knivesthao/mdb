# ailv-code-auth — worked example

## Input

Demo users/roles baked into `scripts/helper.py`: `ada` (admin),
`bob` (viewer), plus unknown user `ghost`.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
password hash (bcrypt in real code): 1cbe9a780065baf3...
ada may delete: ALLOW
bob may delete: DENY
bob may read: ALLOW
ghost may read: DENY
rule: signed-cookie sessions; bcrypt passwords; per-action check, default deny
```
