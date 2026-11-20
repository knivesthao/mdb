# ailv-ui-buttons — worked example

Input: dialog with Cancel (dismissive), Delete (destructive, separated), Save (primary).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: primary last in reading order
PASS: dismissive immediately before primary
PASS: destructive separated from primary
PASS: labels are verbs, not sentences
PASS: targets >= 44px, primary full-width on narrow
demo dialog order [Cancel / Delete / Save] -> buttons-ok
```
