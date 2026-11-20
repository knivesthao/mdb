# ailv-ui-platform-picks — worked example

Input: (react, table), (vue, combo), (react, table, standalone), (angular, dialog).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: ('react', 'table', 'full') -> TanStack Table
PASS: ('vue', 'combo', 'full') -> Headless UI Combobox
PASS: ('react', 'table', 'standalone') -> TanStack Table (Vite/CRA client-only: skip server clauses)
PASS: ('angular', 'dialog', 'full') -> Material dialog
demo: 4 resolves incl. standalone gate -> picks-ok
```
