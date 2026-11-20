# ailv-ops-migrate — worked example

Input: migration `0042_add_email` with 4 steps
(add nullable column, backfill, constrain, drop old column), reversible,
never edited after apply, dry-run ok against prod-shaped data.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: versioned and runs with deploy
PASS: expand then contract, no half-schema
PASS: reversible or paired undo
PASS: never edits an applied migration
PASS: dry-run on prod-shaped data first
migration 0042_add_email: 4 steps, dry-run ok
  1. add nullable column
  2. backfill rows
  3. add constraint
  4. drop old column
```

Exit code: 0. Expand-then-contract with a way back.
