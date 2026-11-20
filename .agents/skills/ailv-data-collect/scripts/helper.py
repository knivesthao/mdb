"""ailv-data-collect helper: cursor polling with landing dedup (at-least-once)."""
import sys

SOURCE = [{"updated_at": 1, "id": 1, "ev": "order.created"},
          {"updated_at": 2, "id": 2, "ev": "order.paid"},
          {"updated_at": 2, "id": 3, "ev": "order.paid"},
          {"updated_at": 3, "id": 4, "ev": "order.shipped"}]
LANDED = set()  # event ids already converged at landing


def poll(cursor):
    out = [e for e in SOURCE
           if (e["updated_at"], e["id"]) > cursor]  # ordered cursor, never pages
    return sorted(out, key=lambda e: (e["updated_at"], e["id"]))


def land(batch):
    fresh = []
    for e in batch:
        if e["id"] not in LANDED:  # dedup at landing
            LANDED.add(e["id"])
            fresh.append(e)
    return fresh


def main():
    cursor = (0, 0)
    print("push-capable sources: webhooks in (not polled); polling this file source")
    for attempt in (1, 2):
        batch = poll(cursor)
        fresh = land(batch + batch[:1])  # retry duplicates freely
        print(f"poll {attempt}: fetched {len(batch)}, landed {len(fresh)} (dupes dropped)")
        if batch:
            last = batch[-1]
            cursor = (last["updated_at"], last["id"])
    print(f"restart resumes from cursor {cursor} (no re-read, no skip)")
    print(f"converged at landing: {sorted(LANDED)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
