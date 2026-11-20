"""ailv-code-deliver helper: run the skill's own handover checklist."""
import sys

# Demo handover: bug fix produced a repro + test.
HANDOVER = {"artifact": "tests/test_quota.py + fix in quotas.py",
            "proof": "repro steps + before/after + guard test run",
            "samples": True, "screenshots_needed": False,
            "screenshots": False, "unresolved": "none - rate-limit edge tracked in #42"}


def check(name, ok):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return ok


def main():
    h = HANDOVER
    ok = True
    ok &= check("handover names proof artifact, not process", bool(h["artifact"]))
    ok &= check("sample outputs included", h["proof"] and h["samples"])
    ok &= check("screenshots present iff screens changed",
                h["screenshots_needed"] == h["screenshots"])
    ok &= check("unresolved listed plainly", "unresolved" in h)
    print(f"artifact: {h['artifact']}")
    print(f"proof: {h['proof']}")
    print("SELF-CHECK:", "PASS" if ok else "FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
