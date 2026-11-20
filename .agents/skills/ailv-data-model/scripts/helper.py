"""ailv-data-model: data shaped for agent readers (demo)."""
from datetime import datetime, timezone

def depth(o, d=1):
    if isinstance(o, dict) and o:
        return max([d] + [depth(v, d + 1) for v in o.values()])
    if isinstance(o, list) and o:
        return max([d] + [depth(v, d + 1) for v in o])
    return d

def check(record):
    fails = []
    if depth(record) > 2:
        fails.append("nested-too-deep")
    if "amt" in record:
        fails.append("tribal-abbrev: amt -> amount_cents")
    if record.get("status") is None and "status" not in record:
        fails.append("null-means-something: use explicit status")
    ts = record.get("created_at_utc", "")
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            fails.append("time-not-utc")
    except Exception:
        fails.append("time-not-iso8601")
    return fails

def main():
    good = {"user_id": 1, "amount_cents": 500, "status": "active",
            "created_at_utc": "2026-01-01T00:00:00Z"}
    bad = {"amt": 5, "meta": {"a": {"b": {"c": 1}}}, "created_at_utc": "yesterday"}
    f1, f2 = check(good), check(bad)
    print(f"GOOD fails={f1} -> {'PASS' if not f1 else 'FAIL'}")
    print(f"BAD fails={f2} -> {'PASS blocked' if f2 else 'FAIL'}")
    print("PASS" if not f1 and len(f2) >= 2 else "FAIL")

if __name__ == "__main__":
    main()
