# Example: legal leaf router

Input: 4 demo tasks run with `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
PASS: 'publish refund policy page' -> ailv-app-legal-pages (want ailv-app-legal-pages)
PASS: 'card entry iframes for SAQ A' -> ailv-app-card-scope (want ailv-app-card-scope)
PASS: 'EU VAT on digital sale' -> ailv-app-tax (want ailv-app-tax)
PASS: 'newsletter opt-out wording' -> ailv-app-legal-mail (want ailv-app-legal-mail)
PASS: exactly one leaf per task
RESULT: PASS
```

Each task routes to exactly one leaf; exit 0.
