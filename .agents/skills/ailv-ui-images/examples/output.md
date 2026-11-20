# ailv-ui-images — worked example

Input: hero.avif (above fold), detail-1.avif (below fold), divider.svg (decorative).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: one above-fold visual
PASS: hero eager + high priority + dims
PASS: below-fold lazy with srcset
PASS: alt on informative, empty-alt on decorative
PASS: no decorative content images
demo: 1 eager hero + 1 lazy detail + 1 decorative -> images-ok
```
