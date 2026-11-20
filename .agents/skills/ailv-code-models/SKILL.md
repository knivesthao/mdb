---
name: ailv-code-models
description: "The harness fixes the model, never the skill: tier the task, match the effort."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Cheapest capable model per task

`ailv-code-models` (Tier the task, not the model): Route every task to a tier before starting: light, workhorse, or frontier — then use whatever model your harness offers at that effort, cheapest first. Light: Q&A and onboarding, docs and commit messages, extraction and log parsing, unit tests, tiny edits, context compaction and repo indexing. Workhorse: routine coding, code review, UI and frontend styling, test generation and QA, single-file refactors. Frontier: complex features and architecture, security reviews, debugging that beat light, multi-file refactors, database migrations and schema design. The harness fixes the model, never the skill: pick the session by tier before the work starts, and never block when an exact model is unavailable — smallest/fastest for light, default for workhorse, most capable for frontier. Escalate on failure only: step up one tier after 2 failed verification or test attempts. Complex features go spec-first: frontier writes the plan only, clear context, then workhorse executes it. Spend rules that compound: keep static repo context at the top of the prompt so repeat turns hit cached reads; run compaction before a session outgrows the provider's standard context tier; work from local copies and never refetch mid-task. Routing multiplies ailv-code-token savings: fewer tokens per step at the right tier.

## Checks

- tier picked before the model on every task
- light serves reads, docs, unit tests, tiny edits, compaction
- frontier reserved for architecture, security, migrations, multi-file work
- escalation steps up one tier after 2 failed attempts, never opens at frontier
- spec-first on frontier, execution on workhorse
- session picked by tier; unavailable models never block
- static context stays top-of-prompt for cache hits
- compaction runs before the context tier steps rates up
