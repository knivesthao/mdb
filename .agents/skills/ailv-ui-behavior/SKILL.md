---
name: ailv-ui-behavior
description: "Explicit text states make every outcome checkable by agents and humans alike, with no interpretation needed."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Behavior contract

`ailv-ui-behavior` (Behavior contract): Every mutation needs an explicit state: idle → working → done|error. Show text status, never color alone. Respect prefers-reduced-motion. Confirm destructive actions inline. Humans verify by looking; log the state string for agents. For standard widgets (dialog, menu, combo, toggle, disclosure) follow the ARIA Authoring Practices pattern, keyboard behavior included — never invent interactions the platform already defined. Guard async transitions: prefetch on intent but serve cached readiness only while fresh (timestamp it, expire it); single-flight concurrent triggers so double-click mounts once; lock re-entrant actions while working. A cached promise is a state — it goes stale like any other. Finish where the user stands: the completed step shows its result plus the exact next action, pre-filled — never a pointer back to where they could assemble it. Recognition over recall (Nielsen heuristic #6): filled values beat fetched instructions. Cover the empty, the broken, and the offline: every list states its empty case, every fetch states its error with a retry, every offline-capable screen says so — no blank regions, no silent failures. Write the error for the human, log the detail for the agent: say what happened, why it matters, and the exact next step — plain words, no codes, no blame. Technical detail (codes, traces, ids) goes to the log, never the screen. Design for touch and flaky networks: every hover-only affordance gets a tap equivalent, and loading and offline states are first-class — most sessions arrive on a phone.

## Checks

- each action exposes a text status
- reduced-motion honored
- destructive action confirms
- async triggers single-flight with fresh cache, re-entrancy locked
- completed steps carry the pre-filled next action
- errors say what happened, why, and the next step
- hover affordances work by tap, loading/offline states shown
