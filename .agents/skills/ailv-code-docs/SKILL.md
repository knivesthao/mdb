---
name: ailv-code-docs
description: "Docs are runtime context — write for the agent, keep the human."
sources:
  - title: Divio documentation system
    url: https://docs.divio.com/documentation-system/
  - title: llms.txt spec
    url: https://llmstxt.org/
  - title: agents.md
    url: https://agents.md/
helper: scripts/helper.py
example: examples/output.md
---

# Write documentation agents can read

`ailv-code-docs` (Documentation agents can read): Your reader is an agent with your page as its only context; a human may read it too, but the human judges verdicts while the agent needs particulars. Generate, don't hand-write: references derive from source (API schemas from models, indexes and sitemaps from route lists) so the documented shape and the enforced shape can never disagree — nothing is copied by hand between two places. One shape per fact: the same fields in the same order everywhere, tables over prose, inputs and outputs stated up front, stable identifiers that never change, and no fact worded two ways. Disclose progressively: a small map routes to leaves, and the agent fetches only what matches — never the whole corpus. End every doc in a check the runner can execute; write the check first and let the paragraph above it be the check explained. Version and sign releases so an agent can confirm what it fetched is what was published. Keep document kinds separate — tutorials, how-tos, generated reference, explanation — each doing one job. Skip everything else.

## Checks

- reference generated from source, never hand-synced
- uniform field shapes and stable identifiers throughout
- no fact worded two ways in two places
- every doc ends in an executable check
- releases versioned and signed
- pages light enough to load fast on phones
