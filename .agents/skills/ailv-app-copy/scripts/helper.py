"""Self-check: mission copy rules on a demo draft."""
import re

BANNED = ["revolutionary", "cutting-edge", "game-changing", "seamless", "unlock"]
ABSOLUTES = ["every dollar", "zero overhead", "zero cost", "100%"]
COPY = """Greenlight Readers

**Who we are:** former teachers in Kisumu running night reading clubs.

**Problem:** 40 pupils share 3 books after school.
**Cost:** repeat rates rose 12% last year at two partner schools.
**Solution:** we lend offline e-libraries with 200 books on low-cost phones.

- Kisumu Night Clubs: weekly clubs for 120 pupils
- Phone Library: 30 preloaded phones lent per term

Give $25 to fund one phone for a term. Gifts are not tax-deductible.
Donate $50 to keep a club running for a month."""

CHECKS = []


def run_checks():
    low = COPY.lower()
    out = []
    out.append(("no banned adjectives", not any(b in low for b in BANNED)))
    out.append(("no absolute money claims", not any(a in low for a in ABSOLUTES)))
    ctas = re.findall(r"(?i)(give|donate)\s+\$\d+", COPY)
    out.append(("at most two CTAs, each with price", 0 < len(ctas) <= 2))
    out.append(("tax status stated where gifts asked",
                "tax-deductible" in low or "tax deductible" in low))
    out.append(("no preamble or meta-talk", not low.startswith("here is")))
    paras = [p for p in COPY.split("\n\n") if p.strip()]
    out.append(("paragraphs of 1-3 sentences",
                all(len(re.split(r"[.!?]\s+", p.strip())) <= 3 for p in paras)))
    return out


def main():
    ok = True
    for name, passed in run_checks():
        print(("PASS" if passed else "FAIL") + f": {name}")
        ok = ok and passed
    print("RESULT:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
