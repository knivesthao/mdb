"""ailv-code-design helper: abuse-story checklist self-check."""
CHECKS = [
    ("abuse story written per feature", True),
    ("default deny, least privilege", True),
    ("costly endpoints rate-limited", True),
    ("upload size capped", False),
    ("response size capped", True),
]

FEATURE = {"name": "avatar upload", "who_pays": "us (storage+bw)",
           "who_hurt": "viewers of forged images", "abuse": "10GB uploads looped"}


def main():
    print("feature: " + FEATURE["name"])
    print("who pays: " + FEATURE["who_pays"] + "; who is hurt: " + FEATURE["who_hurt"])
    print("abuse: " + FEATURE["abuse"])
    failed = 0
    for name, ok in CHECKS:
        print(("PASS " if ok else "FAIL ") + name)
        failed += not ok
    print("result: " + str(len(CHECKS) - failed) + "/" + str(len(CHECKS)) + " checks pass")


if __name__ == "__main__":
    main()
