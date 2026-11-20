# ailv-code-polyglot — worked example

Input (demo, baked into `scripts/helper.py`): seam contract
`PriceQuote{sku: string, cents: int}` and the recorded fixture
`{sku: WIDGET, cents: 2500}`.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
seam contract (generated, not hand-written x2): {"name": "PriceQuote", "fields": {"sku": "string", "cents": "int"}}
PASS  recorded fixture validates in caller language
guest native result (hot path only): {'total': 5000}
guest suite: go test ./quote ... ok (native command, own repo)
```

Reading: one contract generates both sides, the recorded fixture is
tested in the caller's language, the guest side stays a small hot path
proven by its own native suite. Exit code 0.
