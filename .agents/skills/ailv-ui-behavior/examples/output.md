# ailv-ui-behavior — worked example

Input: demo save action (idle → working → done), failing action, cache TTL, confirm gate.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: idle -> working -> done|error only
PASS: single-flight: cached second trigger
PASS: text status shown, never color alone
PASS: destructive confirm gate present
PASS: error says what/why/next, detail logged not shown
PASS: failed action keeps entered data + retry
demo action: idle->working->done, error keeps data -> behavior-ok
```
