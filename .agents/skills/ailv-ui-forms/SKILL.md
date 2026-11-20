---
name: ailv-ui-forms
description: "Every extra click and scroll loses users; the right control asks nothing extra."
sources:
  - title: Baymard checkout research
    url: https://baymard.com/research/checkout-usability
helper: scripts/helper.py
example: examples/output.md
---

# Pick the right input

`ailv-ui-forms` (Pick the right input): For 2 to 4 options use radio buttons or segmented controls — everything visible, one click to answer. Use dropdowns only for 5 to 10 familiar options where space matters. Past 15 items use a combo box: a text input with live filtering so typing 2 or 3 characters isolates the target. For familiar data like birth years use plain numeric inputs. Desktop hover menus wait 300 to 500 milliseconds before opening; prefer click-to-open menus. Type with thumbs: inputs at least 44px tall, numeric keyboards for numeric fields (inputmode), native pickers or full-screen sheets for dropdowns on phones — never disable pinch zoom. When one option suits most users, show it as the combo box default. Errors live where the eyes are: failed submits name every bad field inline at the field, announce the count at the top, and keep all entered data — never a bare toast, never wiped forms. One question, one answer: when presets and a custom field feed the same value, they stay mutually exclusive — typing custom clears the presets, picking a preset clears custom. Never show two claimed answers at once.

## Checks

- short lists use radio, not dropdowns
- 15+ items get combo or text input
- hover menus carry 300-500ms delay
- preset and custom never both claim the value
- 44px inputs, inputmode set, zoom never disabled
