---
name: ailv-verify-tests
description: "Tests are the only verdict both humans and agents can trust without reading the code."
---

# Tests are the spec

`ailv-verify-tests` (Tests are the spec): Humans judge by tests, not by reading code. Ship one runnable check per behavior: one command (`./run.sh test`, `pytest`) must pass. Cover happy path + one edge (empty, oversized, unauthorized). Print PASS/FAIL lines an agent can parse. Quarantine flakes: a test that fails with no code change leaves the suite with its failure log attached — rerun it alone, fix or delete it within the week, never retry it blindly in place. Assert redirect behavior explicitly — test clients follow redirects by default, so a silent 200 can hide a missing gate; pass follow_redirects=False (or the client's equivalent) and assert the redirect status itself. Write tests type-clean by construction: intentional invalid-input tests go through `Model.model_validate({...})` with a dict, never `Model(bad=...)` — same boundary, no checker trip, no ignore needed. Assert non-null before attribute access on nullable lookups. When the task writes test files, read this skill at the start of the test-writing phase and keep it for every test step — not just the review checkpoint. This skill is its own guide: when no verify index exists for the area, read this skill first and let its checks (one command, edge covered, parseable output) stand as the test plan.

## Checks

- one command runs all checks
- edge case covered
- output is parseable
- redirects asserted explicitly, never followed silently
- invalid-input tests use model_validate dict form; nullable lookups asserted
