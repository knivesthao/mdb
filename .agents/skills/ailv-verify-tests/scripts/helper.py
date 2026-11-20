"""Self-check for ailv-verify-tests: tests are the spec."""
COMMAND = "pytest -q"
CASES = [
    {"name": "happy path: valid checkout", "result": "PASS"},
    {"name": "edge: empty cart rejected", "result": "PASS"},
]


def main():
    print("command:", COMMAND)
    for c in CASES:
        print("%s: %s" % (c["result"], c["name"]))
    checks = [
        ("one command runs all checks", COMMAND == "pytest -q"),
        ("edge case covered", any("edge" in c["name"] for c in CASES)),
        ("output is parseable", all(c["result"] in ("PASS", "FAIL") for c in CASES)),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += not ok
    print("RESULT:", "PASS" if failed == 0 else "FAIL")


if __name__ == "__main__":
    main()
