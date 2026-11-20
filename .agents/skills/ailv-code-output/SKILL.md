---
name: ailv-code-output
description: "Done work earns its screen space: code proves, writing shows, research cites — never a process summary."
---

# Show what the work earned

`ailv-code-output` (Show what the work earned): When work is done, match what the user sees to what was done — never a process summary. Code shipped → `ailv-code-deliver` first: a clickable link per changed file with its line range, plus test evidence and proof it ran — never a pasted diff, nobody is doing code review. Docs or content written → a tight summary plus where it lives; the full piece only on request — never dump the whole text into context. Research finished → claims with sources, never the search trail. Data touched → counts and samples, never the pipeline log. Blocked or failed → what's blocked, why the requested input unblocks it, and the choice in the harness's own permission form — yes/no, or allow / allow-once / deny where supported. No autopsy unless asked. Routine confirmations → no line at all when a tool result or visible change already proves it; a bare confirmation only when no other signal exists. Internal deliberation stays internal: never narrate the choosing — emit the decision plus its evidence, not the reasoning trail. Routine steps report as one line (executing plan), never a paragraph. Mixed work → each kind in its own shape, shortest first. Reviews and summaries → verdict first, then three fixed lines every time: what changed, what proves it, what remains. Reviews stay under 60 words — the doc is linked, not repeated. Code changes never ship as pasted diffs — the agent does all the coding and nobody reads generated diffs. Whole-task builds end in a verdict plus proof the work ran, with no file links and no diffs. Small changes (1–4 files touched) link each file with its line range so the user opens it in their editor's own diff tool — links, never pasted code. No scaffolding beyond the step's checks; when the checks pass, stop writing. Fixes are not output: they follow ailv-code-token — patch the exact lines (edit_file), never re-emit a whole module for a local defect. Between steps and subagents, pass pointers, never code: path:start-end plus function signatures and one-line behavior bullets — no pasted snippets. Reviews, audits, and test failures report strictly as PASS or FAIL: <path:start-end> — <issue> — <fix>.



## Checks

- output shape matches the work done
- no process summary stands in for proof
- pieces summarized with location, full text on request only
- reviews under 60 words, the doc is linked
- blocked states carry the why plus a yes/no or allow-once choice
- no confirmation line where the result is already visible
- changed files linked with lines, never diff-dumped
- no pasted diffs, ever
- fixes patch exact lines per ailv-code-token, never whole modules
- whole-task builds: verdict plus proof, no file links
- small changes link each file, never paste code
- no narrated deliberation; decisions plus evidence only
- no code beyond the step's scope
- step and subagent handoffs pass pointers, never pasted code
- reviews and failures report PASS or FAIL: path — issue — fix
