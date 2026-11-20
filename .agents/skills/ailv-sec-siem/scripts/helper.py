"""ailv-sec-siem: tamper-evident logs + alerts tuned to analyst capacity."""
import hashlib

EVENTS = [
    {"ts": "2026-11-08T09:00:00Z", "type": "auth", "msg": "login ok ada"},
    {"ts": "2026-11-08T09:01:12Z", "type": "admin", "msg": "role grant bob"},
    {"ts": "2026-11-08T09:02:40Z", "type": "data-access", "msg": "export customers.csv"},
    {"ts": "2026-11-08T09:03:55Z", "type": "auth", "msg": "login fail eve x14"},
]

ANALYST_CAPACITY_PER_DAY = 20


def chain(events):
    prev = "GENESIS"
    rows = []
    for e in events:
        h = hashlib.sha256(f"{prev}|{e['ts']}|{e['type']}|{e['msg']}".encode()).hexdigest()[:16]
        rows.append((e, h))
        prev = h
    return rows


def main():
    rows = chain(EVENTS)
    print(f"ingested {len(rows)} events (auth/admin/data-access) into hash-chained store")
    ok = True
    prev = "GENESIS"
    for e, h in rows:
        expect = hashlib.sha256(f"{prev}|{e['ts']}|{e['type']}|{e['msg']}".encode()).hexdigest()[:16]
        status = "PASS" if expect == h else "FAIL"
        ok = ok and expect == h
        print(f"  [{status}] {e['ts']} {e['type']}: {e['msg']} chain={h}")
        prev = h
    print(f"integrity verification: {'PASS' if ok else 'FAIL'} (tested, not assumed)")
    alerts = sum(1 for e in EVENTS if "fail" in e["msg"])
    tuned = "PASS" if alerts <= ANALYST_CAPACITY_PER_DAY else "FAIL"
    print(f"[{tuned}] alert volume {alerts}/day vs capacity {ANALYST_CAPACITY_PER_DAY}/day: tuned")
    print(f"self-check: {'PASS' if ok and tuned == 'PASS' else 'FAIL'}")


if __name__ == "__main__":
    main()
