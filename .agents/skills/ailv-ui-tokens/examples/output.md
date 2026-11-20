# ailv-ui-tokens — worked example

Input: tokens `--ink #1a1a1a`, `--paper #ffffff`, `--accent #005fcc`; spacing 4/8/16/32.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: palette is 3 colors max
PASS: no per-element color decisions (token refs only)
PASS: contrast ink/paper 17.4:1 >= 4.5
PASS: spacing scale 4/8/16/32 holds
PASS: touch targets reach 44px
demo tokens: ink/paper/accent, contrast 17.4:1 -> tokens-ok
```
