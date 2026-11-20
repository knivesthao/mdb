---
name: ailv-code-reasoning
description: "Reasoning stays hidden; the user sees decisions and proof."
sources:
  - title: Anthropic context engineering
    url: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
helper: scripts/helper.py
example: examples/output.md
---

# Hidden reasoning, visible proof

`ailv-code-reasoning` (Hidden reasoning, visible proof): Reason internally, show only what the work earned — never the thinking trail. Applies to any IDE or harness, never one panel: Zed, terminal, web, anywhere an agent renders output. Collapse reasoning by default; routine steps report as one line; decisions ship with evidence, never narration of the choosing. Full trace goes to a local log excluded from model context, for human debugging only. Small reasoning budget for simple tasks, larger only on failure or complex plans.

## Checks

- reasoning hidden by default in every harness
- no narrated deliberation; decisions plus evidence only
- routine steps one line, never a paragraph
- full trace in local log, log excluded from context
- per-run token meter recorded
- fixes are smallest edits per ailv-code-token, never whole-file rewrites
