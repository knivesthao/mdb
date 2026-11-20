# ailv-code-legacy — worked example

Input (demo, baked into `scripts/helper.py`): strangler slices moving
the replacement from 0% to 100% of traffic behind the old interface,
with a legacy `A-1`-style SKU quirk normalized in an anti-corruption
layer.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
slice new=0%: ['old', 'old', 'old', 'old']
slice new=10%: ['old', 'old', 'new', 'old']
slice new=50%: ['new', 'old', 'new', 'old']
slice new=100%: ['new', 'new', 'new', 'new']
existing patterns followed first; dead old path deleted after 100% + clean drills
flag-day rewrite: no
```

Reading: traffic moves slice by slice, the legacy quirk never leaks
into the new code, and the old path is deleted only after carrying
100% with clean drills — no flag-day rewrite. Exit code 0.
