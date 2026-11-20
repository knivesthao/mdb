---
name: ailv-code-plan
description: "One batched fetch plus parallel independents beats sequential steps that each re-read."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Plan once, fetch once, run wide

`ailv-code-plan` (Plan once, fetch once, run wide): Count the task-matched skills — the always-on skills and the maps don't count, they're fixed overhead. Crossing area maps is free — only matched leaves count. One or two — execute directly, no plan, unless it is the first file of its kind — that always plans: read the area index, name the done-state, then execute. Three or more — write the numbered plan before executing: inline if five steps or fewer in one live session, file if longer or interruptible. Each step names its skill and its exact done-state. Mark each step independent or blocked (naming the step it waits for); split mixed UI-plus-service jobs into per-track steps, each naming only its track's skills; execute all unblocked steps together, sequential only where one step's output feeds the next. Fetch every named skill once during planning, in one batched request — execution fetches nothing. If a step fails, fix the step — never rewrite the plan mid-flight without saying why. The last step is always cleanup: delete the plan file and every scratch file this task created — the tree holds only the deliverable plus its tests. Never delete anything you did not create; close with a structured final report — one record per step (task, result, artifact link), never prose; name anything uncertain in it instead of removing it.

## Checks

- file only when long or interruptible
- independents run together, dependents wait
- all skills fetched once up front, none during execution
- tree holds only deliverable plus tests
