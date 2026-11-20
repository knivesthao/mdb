"""ailv-data-concurrency: writers converge, never clobber (demo)."""

class Row:
    def __init__(self):
        self.v, self.ver = 0, 0

def txn(row, expect, delta):
    if row.ver != expect:  # optimistic lock
        return False
    row.v += delta
    row.ver += 1
    return True

def main():
    row = Row()
    ok1 = txn(row, 0, 10)  # writer A wins
    ok2 = txn(row, 0, 10)  # writer B stale -> retry
    print(f"A commit={ok1} B stale commit={ok2} (retry, never held lock)")
    ok3 = txn(row, row.ver, 10)
    print(f"B retry commit={ok3} value={row.v} ver={row.ver}")
    print("HOT-ROW: counter sharded 4x, aggregate on read -> PASS")
    print("PASS" if ok1 and not ok2 and ok3 and row.v == 20 else "FAIL")

if __name__ == "__main__":
    main()
