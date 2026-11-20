# ailv-ui-a11y — worked example

Input: 3-step flow (search, add-to-cart, checkout) with landmarks, ordered headings, live regions, chart twin, static motion equivalents.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: keyboard: tab order matches visual
PASS: keyboard: every control reachable + operable
PASS: keyboard: focus visible, traps only modal w/ escape
PASS: screen reader: landmarks + ordered headings + live regions
PASS: screen reader: charts expose data twin
PASS: reduced motion fully honored (static equivalents)
demo flow (3 steps) keyboard+ears+motion-off -> a11y-ok
```
