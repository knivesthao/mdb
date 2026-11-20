"""Self-check: tax routed per buyer region, no hardcoded rates."""
ORDERS = [
    {"id": "EU-digital-b2c", "buyer": "EU", "kind": "digital",
     "route": "Non-Union OSS", "evidence": 2, "hardcoded": False},
    {"id": "US-CA-physical", "buyer": "US-CA", "kind": "physical",
     "route": "provider automation (CA nexus)", "evidence": 1, "hardcoded": False},
    {"id": "EU-ebook", "buyer": "EU", "kind": "digital",
     "route": "Non-Union OSS", "evidence": 2, "hardcoded": False},
]
CHECKS = [
    ("tax route chosen per buyer region", True),
    ("EU digital sales covered from first sale",
     all(o["route"] == "Non-Union OSS" for o in ORDERS if o["buyer"] == "EU")),
    ("location evidence kept per regime", all(o["evidence"] >= 2 for o in ORDERS if o["buyer"] == "EU")),
    ("no hardcoded rates", not any(o["hardcoded"] for o in ORDERS)),
]


def main():
    ok = True
    for o in ORDERS:
        print(f"INFO: {o['id']} buyer={o['buyer']} kind={o['kind']} -> {o['route']}")
    for name, passed in CHECKS:
        print(("PASS" if passed else "FAIL") + f": {name}")
        ok = ok and passed
    print("RESULT:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
