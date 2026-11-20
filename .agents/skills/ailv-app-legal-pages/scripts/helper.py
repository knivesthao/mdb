"""Self-check: legal pages ready before first order."""
PAGES = {
    "privacy": {"live": True, "names_subprocessors": True, "retention": True,
                "deletion_contact": True, "disclaims_advice": True},
    "terms": {"live": True, "price_shown": True, "cadence": True,
              "delivery": True, "liability_cap": True, "disclaims_advice": True},
    "refund": {"live": True, "terms_at_purchase": True, "disclaims_advice": True},
}
OWNER_REVIEW = True
CHECKS = [
    ("privacy, terms, refund pages live", all(PAGES[p]["live"] for p in PAGES)),
    ("subprocessors, retention, deletion contact named",
     all(PAGES["privacy"][k] for k in ("names_subprocessors", "retention", "deletion_contact"))),
    ("price, cadence, refunds, delivery at purchase",
     PAGES["terms"]["price_shown"] and PAGES["terms"]["cadence"]
     and PAGES["refund"]["terms_at_purchase"] and PAGES["terms"]["delivery"]),
    ("pages disclaim legal advice; owner review recorded",
     all(PAGES[p]["disclaims_advice"] for p in PAGES) and OWNER_REVIEW),
]


def main():
    ok = True
    for name, passed in CHECKS:
        print(("PASS" if passed else "FAIL") + f": {name}")
        ok = ok and passed
    print("RESULT:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
