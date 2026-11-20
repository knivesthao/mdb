# ailv-verify-visual — worked example

Input: demo screen baked into `scripts/helper.py` (orders screen with
3 real seeded orders, error-state banner, desktop + 360px shots).

Run: `python3 scripts/helper.py` from inside the skill folder.

Actual output:

```
screen: orders screen with 3 real seeded orders (no lorem, no empty list)
eyeball items: layout, labels, error state
error state: empty-card banner visible with retry button
shots: shots/orders-desktop.png, shots/orders-360.png
PASS: seeded demo data present
PASS: 3 eyeball items listed
PASS: error state visible
PASS: desktop and 360px shots saved
RESULT: PASS
```

Exit code 0. Real browser or the user's screenshot stays the proof.
