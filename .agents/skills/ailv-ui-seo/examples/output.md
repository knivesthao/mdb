# ailv-ui-seo — worked example

Input: page "Trail shoes that grip wet rock" (title 30 chars, description 60 chars, 1 H1); 3 public + 3 walled pages.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: one H1 (found 1)
PASS: title 30 chars < 60
PASS: description 60 chars < 160
PASS: real links, never JS-only nav
PASS: sitemap lists 3 public pages
PASS: paid pages noindexed + out of sitemap
demo page: title/desc lengths ok, sitemap 3 public, 3 walled noindex -> seo-ok
```
