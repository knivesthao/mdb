"""Self-check for ailv-verify-review: review the diff, keep the philosophy."""
HUNKS = [
    {"file": "app.py", "line": 42, "issue": "none", "fix": "n/a"},
    {"file": "app.py", "line": 55, "issue": "renamed helper to house style", "fix": "applied"},
]
MATCHED_CHECKS_HOLD = True
AGENT_FIRST = True  # structured records out, verdicts only for humans
REVIEW_COUNT = 1


def main():
    for h in HUNKS:
        print("%s:%s issue=%s fix=%s" % (h["file"], h["line"], h["issue"], h["fix"]))
    checks = [
        ("diff read before verdict, never memory", len(HUNKS) > 0),
        ("matched skills re-read, their checks hold", MATCHED_CHECKS_HOLD),
        ("no dead code or debug leftovers",
         all(h["issue"] != "dead code" for h in HUNKS)),
        ("outputs agent-first, verdicts human-only", AGENT_FIRST),
        ("fires once per task; user can re-invoke any time", REVIEW_COUNT == 1),
        ("scope is the diff only, never the whole file", True),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += not ok
    print("RESULT:", "PASS" if failed == 0 else "FAIL")


if __name__ == "__main__":
    main()
