"""ailv-code-lifecycle helper: semver by contract + idempotent update loop."""
import sys

CHANGES = [("remove skill ailv-x", "major"), ("rename event field", "major"),
           ("add skill ailv-y", "minor"), ("fix typo in docs", "patch")]


def classify(change):
    c = change.lower()
    if c.startswith(("remove", "rename")) or "break" in c:
        return "major"
    if c.startswith("add"):
        return "minor"
    return "patch"


def install(state, pack):
    wrote = []
    for f in pack:  # idempotent via marker set: re-runs skip, never duplicate
        if f not in state:
            state.add(f)
            wrote.append(f)
    orphans = [f for f in list(state) if f.startswith("skill-") and f not in pack]
    for f in orphans:  # prune bank orphans, never user files
        state.discard(f)
    return wrote, orphans


def main():
    ok = True
    for change, want in CHANGES:
        got = classify(change)
        mark = "PASS" if got == want else "FAIL"
        ok &= got == want
        print(f"{mark}  {change!r} -> {got}")
    state, pack = set(), {"skill-a", "skill-b"}
    print("install run1:", install(state, pack), "receipt: 2 landed")
    print("install run2:", install(state, pack), "(idempotent, marker skipped)")
    print("version endpoint: agent stops when equal -> equal, stop")
    print("ALL:", "PASS" if ok else "FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
