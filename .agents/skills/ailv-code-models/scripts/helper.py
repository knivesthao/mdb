"""Tier demo: every task category resolves to light, workhorse, or frontier. Stdlib only."""

TIERS = {
    "light": [
        "q&a / onboarding",
        "docs / commit messages",
        "extraction / log parsing",
        "unit tests / tiny edits",
        "context compaction / repo indexing",
    ],
    "workhorse": [
        "routine coding / boilerplate",
        "code review",
        "ui / frontend styling",
        "test generation / qa",
        "single-file refactors",
    ],
    "frontier": [
        "complex features / architecture",
        "security reviews",
        "debugging that beat light",
        "multi-file refactors",
        "migrations / schema design",
    ],
}

for tier, cats in TIERS.items():
    for cat in cats:
        print(f"{cat:32} -> {tier}")
total = sum(len(cats) for cats in TIERS.values())
print(f"\ncategories: {total}, tiers: 3, escalation: start one down, step up on failure")
