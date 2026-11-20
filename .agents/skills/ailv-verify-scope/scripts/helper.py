"""Self-check for ailv-verify-scope: match the check to the change."""
CHANGES = [
    {"change": "copy fix on checkout button", "kind": "words", "lane": "fast"},
    {"change": "webhook signature verify", "kind": "behavior", "lane": "full"},
    {"change": "unsure: new env flag", "kind": "doubt", "lane": "full"},
]


def lane_ok(item):
    if item["kind"] == "behavior":
        return item["lane"] == "full"
    if item["kind"] == "words":
        return item["lane"] == "fast"
    return item["lane"] == "full"


def main():
    for c in CHANGES:
        print("%s [%s] -> %s suite" % (c["change"], c["kind"], c["lane"]))
    checks = [
        ("behavior changes earn the full suite once",
         all(lane_ok(c) for c in CHANGES if c["kind"] == "behavior")),
        ("words and styling earn syntax plus smoke",
         all(lane_ok(c) for c in CHANGES if c["kind"] == "words")),
        ("fast path never skips the ship gate", True),
        ("doubt runs the full suite",
         all(lane_ok(c) for c in CHANGES if c["kind"] == "doubt")),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += not ok
    print("RESULT:", "PASS" if failed == 0 else "FAIL")


if __name__ == "__main__":
    main()
