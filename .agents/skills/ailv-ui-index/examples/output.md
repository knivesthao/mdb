# ailv-ui-index — worked example

Input: 11 interface task phrases (screen, interactive, chart, widget, mobile, form, buttons, states, nav, image, audit).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: 'new screen' -> ailv-ui-shell, ailv-ui-tokens, ailv-ui-seo
PASS: 'interactive typing' -> ailv-ui-framework
PASS: 'sales chart' -> ailv-ui-charts, ailv-ui-chart-twin
PASS: 'data table widget' -> ailv-ui-widgets, ailv-ui-platform-picks
PASS: 'mobile app' -> ailv-ui-mobile
PASS: 'checkout inputs' -> ailv-ui-forms
PASS: 'dialog buttons' -> ailv-ui-buttons
PASS: 'page states' -> ailv-ui-behavior
PASS: 'header nav' -> ailv-ui-nav
PASS: 'hero image' -> ailv-ui-images
PASS: 'accessibility audit' -> ailv-ui-a11y
demo: 11 tasks routed, none reads the whole area -> router-ok
```
