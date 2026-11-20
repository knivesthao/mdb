---
name: ailv-code-deps
description: "Your code inherits every vulnerability in every library it imports."
sources:
  - title: pip-audit
    url: https://github.com/pypa/pip-audit
  - title: OSV
    url: https://osv.dev/
  - title: Dependabot
    url: https://docs.github.com/en/code-security/dependabot
helper: scripts/helper.py
example: examples/output.md
---

# Dependencies audited

`ailv-code-deps` (Dependencies audited): Pin every dependency (requirements with versions), audit on a schedule (pip audit or equal), and update promptly when a fix lands. Fewer dependencies means fewer advisories: drop what the stack already covers. Never vendor a copy you will forget to patch.

## Checks

- deps pinned with versions
- audit runs on schedule
- unused deps removed
