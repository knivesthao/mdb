# Example: tax routing self-check

Input: 3 demo orders (EU digital x2, US-CA physical) run with `python3 scripts/helper.py`.

Actual output:

```
INFO: EU-digital-b2c buyer=EU kind=digital -> Non-Union OSS
INFO: US-CA-physical buyer=US-CA kind=physical -> provider automation (CA nexus)
INFO: EU-ebook buyer=EU kind=digital -> Non-Union OSS
PASS: tax route chosen per buyer region
PASS: EU digital sales covered from first sale
PASS: location evidence kept per regime
PASS: no hardcoded rates
RESULT: PASS
```

EU digital sales route to OSS from the first sale; exit 0.
