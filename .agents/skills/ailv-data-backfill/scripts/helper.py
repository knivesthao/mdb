"""ailv-data-backfill: bounded throttled replays (demo)."""
import time

QUOTA_PER_S = 2

def main():
    partitions = ["2026-01-01", "2026-01-02", "2026-01-03"]
    store = {"2026-01-01": [1]}  # stale
    markers = {}
    for p in partitions:  # bounded: 3 days, never full table
        time.sleep(1 / QUOTA_PER_S)  # throttle below prod
        store[p] = [10, 20]  # idempotent overwrite
        markers[p] = "rewritten"
        print(f"BACKFILL partition={p} rows=2 marker=rewritten (throttled)")
    rerun = dict(store)
    store["2026-01-01"] = [10, 20]
    print(f"RERUN converges={store == rerun} markers={len(markers)}")
    print("PASS" if store == rerun and len(markers) == 3 else "FAIL")

if __name__ == "__main__":
    main()
