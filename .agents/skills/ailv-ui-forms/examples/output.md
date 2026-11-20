# ailv-ui-forms — worked example

Input: option counts 3 / 7 / 40 / 60(familiar numbers) plus thumb, delay, exclusivity, error rules.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: 3 options -> radio (want radio)
PASS: 7 options -> dropdown (want dropdown)
PASS: 40 options -> combo (want combo)
PASS: 60 options -> numeric-input (want numeric-input)
PASS: hover menus carry 300-500ms delay
PASS: preset/custom mutually exclusive
PASS: 44px inputs, inputmode set, zoom never disabled
PASS: errors inline at field + count at top, data kept
demo: radio/dropdown/combo/numeric routing -> forms-ok
```
