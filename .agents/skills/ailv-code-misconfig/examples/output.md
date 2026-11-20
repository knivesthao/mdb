# ailv-code-misconfig — worked example

## Input

Demo production config baked into `scripts/helper.py` (DEBUG/TRACE off,
HSTS + CSP on, CORS allowlist, no default password, generic error page).

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
DEBUG = False
TRACE = False
HSTS = True
CSP = default-src 'self'
CORS_ORIGINS = ['https://app.example.com']
ADMIN_PASSWORD = **** (no default)
ERROR_PAGE = generic
PASS debug off in production
PASS security headers set
PASS CORS allowlist (no wildcard)
PASS no default passwords
```
