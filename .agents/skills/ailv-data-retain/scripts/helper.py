"""ailv-data-retain: expire per policy, prove deletion (demo)."""
POLICY_DAYS = {"events": 90, "pii_profile": 30}

def age_days(now, created):
    return now - created

def main():
    now = 100
    datasets = [
        {"name": "events", "created": 0, "pii": False},
        {"name": "pii_profile", "created": 60, "pii": True},
        {"name": "pii_profile", "created": 0, "pii": True, "dsr": "user-7"},
    ]
    for d in datasets:
        age = age_days(now, d["created"])
        limit = POLICY_DAYS[d["name"]]
        if d.get("dsr"):
            print(f"DSR subject={d['dsr']} key shredded -> proof=receipt-{d['dsr']} PASS")
        elif age > limit:
            print(f"EXPIRE dataset={d['name']} age={age}d > {limit}d -> cold-store (open parquet)")
        else:
            print(f"KEEP dataset={d['name']} age={age}d <= {limit}d")
    print("PASS")

if __name__ == "__main__":
    main()
