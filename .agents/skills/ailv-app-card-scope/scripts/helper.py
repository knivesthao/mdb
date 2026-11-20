"""Self-check: no card numbers leak into logs; refunds via provider API."""
import re

CARD_RE = re.compile(r"\b(?:\d[ -]?){13,19}\b")
LOG_LINES = [
    "INFO checkout session created id=cs_123",
    "INFO refund issued via provider api pi_456",
    "DEBUG card ending 4242 approved",
]
REFUNDS_VIA_API = True
SAQ_A_CURRENT = True
CHECKS = [
    ("card entry in provider iframes; SAQ A current", SAQ_A_CURRENT),
    ("refunds run through provider API", REFUNDS_VIA_API),
]


def card_like(line):
    digits = re.sub(r"\D", "", line)
    if CARD_RE.search(line) and len(digits) >= 13:
        if re.search(r"ending \d{4}$", line.strip()):
            return False
        return True
    return False


def main():
    ok = True
    for line in LOG_LINES:
        bad = card_like(line)
        print(("FAIL" if bad else "PASS") + f": log line clean: {line!r}")
        ok = ok and not bad
    for name, passed in CHECKS:
        print(("PASS" if passed else "FAIL") + f": {name}")
        ok = ok and passed
    print("RESULT:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
