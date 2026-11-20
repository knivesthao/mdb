---
name: ailv-verify-review
description: "Writing and reviewing use different eyes; the diff read catches dead code, leftover scaffolding, and philosophy drift that tests never assert."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Review the diff, keep the philosophy

`ailv-verify-review` (Review the diff, keep the philosophy): This skill fires automatically after every coding task, before tests — it is always on, never matched. Read the complete diff — never review from memory. Scope is the diff only — never re-litigate unchanged lines; judge old code solely by whether the new hunks integrate with it. Every hunk must serve the task: no dead code, no debug scaffolding left behind, no scope creep, no unrelated cleanup; names match house conventions; secrets never in the repo. Then re-read the skills matched for this task and verify their checks hold on the new code — the review tracks the bank, so new code keeps it in mind. Then the philosophy pass: outputs serve agents first (structured records, typed errors, machine-readable plans — never prose another agent must parse); humans get verdicts only (tests, screenshots, receipts). Generic rules stay generic with the house stack as the example, never the rule. Report findings as records (file, line, issue, fix) — fix what is safe, flag what needs a human. Fires once per coding task — fixes from this pass never trigger another review; the user can invoke review again manually at any time. Read the code to determine what it does and check the right skills were matched — flag matched-but-irrelevant skills and missing skills the code needed.

## Checks

- diff read before verdict, never memory
- matched skills re-read, their checks hold
- no dead code or debug leftovers
- outputs agent-first, verdicts human-only
- fires once per task; user can re-invoke any time
- scope is the diff only, never the whole file
