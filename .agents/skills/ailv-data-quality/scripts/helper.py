"""ailv-data-quality: gate promotion on signals (demo)."""

def gates(batch, prev_mean):
    fails = []
    if not batch.get("fresh_min_ago", 999) <= 60:
        fails.append("stale")
    nulls = sum(1 for r in batch["rows"] if r.get("amount_cents") is None)
    if nulls / max(len(batch["rows"]), 1) > 0.05:
        fails.append(f"nulls={nulls}")
    if len(batch["rows"]) < 10:
        fails.append("volume-drop")
    mean = sum(r.get("amount_cents") or 0 for r in batch["rows"]) / max(len(batch["rows"]), 1)
    if abs(mean - prev_mean) / max(prev_mean, 1) > 0.5:
        fails.append(f"distribution-shift mean={mean:.0f} prev={prev_mean}")
    return fails, mean

def main():
    good = {"fresh_min_ago": 5, "rows": [{"amount_cents": 100}] * 20}
    f1, m = gates(good, 100)
    print(f"GOOD fails={f1} -> {'PASS promote' if not f1 else 'FAIL'}")
    bad = {"fresh_min_ago": 5, "rows": [{"amount_cents": None}] * 3 + [{"amount_cents": 99999}] * 7}
    f2, _ = gates(bad, 100)
    print(f"BAD fails={f2} -> {'BLOCKED page owner + sample attached' if f2 else 'FAIL: passed bad data'}")
    print(f"ROW-COUNT-ONLY would pass bad batch: volume={len(bad['rows'])} -> signals win -> PASS")
    print("PASS" if not f1 and f2 else "FAIL")

if __name__ == "__main__":
    main()
