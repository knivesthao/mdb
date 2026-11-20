"""ailv-data-ingest: land every event exactly once (demo)."""
import time

SCHEMA = {"event_id": str, "amount_cents": int}
DEDUP_TTL_S = 3600

def main():
    dedup = {}  # key -> timestamp
    store = []
    dlq = []
    demo = [
        {"key": "evt-1", "event_id": "evt-1", "amount_cents": 500},
        {"key": "evt-1", "event_id": "evt-1", "amount_cents": 500},  # retry
        {"key": "evt-2", "event_id": "evt-2", "amount_cents": 700, "note": "additive ok"},
        {"key": "evt-3", "event_id": "evt-3"},  # poison: missing field
    ]
    for ev in demo:
        key = ev["key"]
        if key in dedup and time.time() - dedup[key] < DEDUP_TTL_S:
            print(f"DEDUP skip key={key} (retry converged)")
            continue
        body = {k: v for k, v in ev.items() if k != "key"}
        extra = set(body) - set(SCHEMA)
        if extra:
            print(f"ADDITIVE pass-through key={key} extra={sorted(extra)}")
        missing = [f for f in SCHEMA if f not in body]
        if missing:
            print(f"POISON key={key} missing={missing} -> DLQ")
            dlq.append(ev)
            continue
        dedup[key] = time.time()
        store.append(body)
    print(f"STORE rows={len(store)} dlq={len(dlq)} dedup_keys={len(dedup)}")
    print("PASS" if len(store) == 2 and len(dlq) == 1 else "FAIL")

if __name__ == "__main__":
    main()
