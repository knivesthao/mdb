"""Self-check: transactional vs marketing mail consent rules."""
MAILS = [
    {"id": "order receipt", "kind": "transactional", "consent": False,
     "has_marketing": False, "opt_out": False, "ok": True},
    {"id": "sale newsletter", "kind": "marketing", "consent": True,
     "has_marketing": True, "opt_out": True, "ok": True},
]
SUPPRESSION_KEPT = True
LISTS_MERGED = False
CHECKS = [
    ("order mail transactional-only, no marketing inside",
     all(m["kind"] != "transactional" or not m["has_marketing"] for m in MAILS)),
    ("marketing needs prior consent plus working opt-out",
     all(m["consent"] and m["opt_out"] for m in MAILS if m["kind"] == "marketing")),
    ("buyer lists never merged into marketing", not LISTS_MERGED),
    ("suppression list kept indefinitely", SUPPRESSION_KEPT),
]


def main():
    ok = True
    for m in MAILS:
        print(f"INFO: {m['id']} kind={m['kind']} consent={m['consent']} opt_out={m['opt_out']}")
    for name, passed in CHECKS:
        print(("PASS" if passed else "FAIL") + f": {name}")
        ok = ok and passed
    print("RESULT:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
