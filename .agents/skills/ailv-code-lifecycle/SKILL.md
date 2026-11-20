---
name: ailv-code-lifecycle
description: "A bank with no uninstall rots; one stale skill poisons every agent that installs it."
sources:
  - title: Semantic Versioning
    url: https://semver.org/
  - title: Keep a Changelog
    url: https://keepachangelog.com/en/1.1.0/
  - title: Conventional Commits
    url: https://www.conventionalcommits.org/en/v1.0.0/
helper: scripts/helper.py
example: examples/output.md
---

# Version, pin, retire

`ailv-code-lifecycle` (Version, pin, retire): Pin every installed skill to its version; check for updates on a schedule, never silently auto-update. Verify the bank's signature before installing — provenance first, content second. Deprecate before removing: mark superseded, point at the replacement, delete after one release — never vanish a skill agents depend on. Retire skills the field stops using; a bank that only grows stops being read. Version by contract (semver): major when you break the contract — remove or rename anything consumers depend on, or change what an existing surface means, so consumers must re-read; minor when you add without breaking — safe to skip; patch for fixes and wording that change no behavior. Applied to a skill bank: removing or renaming a skill is major, adding one is minor. Bank minors stay safe because the installer rewrites files and prunes orphans instead of patching in place. Ship an update loop, not just versions: publish a version endpoint agents check first and stop when equal; write installs idempotently from a marker file — re-runs skip what is written, never duplicate; report receipts so the publisher knows what landed; prune files the new pack no longer contains, never touching user files. This skill governs the bank itself, including this skill.

## Checks

- installed skills pinned and signed
- deprecate-then-remove, never vanish
- retired skills actually deleted
- version bump matches the contract change (major/minor/patch)
- update loop present: version check, marker file, idempotent writes, receipts, orphan prune
