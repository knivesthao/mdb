# ailv-ui-shell — worked example

Input: header/main/footer shell with one icon-only button (`aria-label`, `data-action`, Lucide icon).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: <header> landmark present
PASS: <main> landmark present
PASS: <footer> landmark present
PASS: every control labeled
PASS: custom controls expose data-action
PASS: lucide icons, no hand-written svg
demo shell: header/main/footer + labeled icon button -> shell-ok
```
