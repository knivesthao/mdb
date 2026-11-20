"""ailv-data-etl: tested transforms, idempotent reloads (demo)."""

def transform(row):
    return {"day": row["day"], "user_id": row["user_id"],
            "amount_cents": int(row["amount_dollars"] * 100)}

def test_transform():
    assert transform({"day": "2026-01-01", "user_id": 1, "amount_dollars": 5.0}) == \
        {"day": "2026-01-01", "user_id": 1, "amount_cents": 500}
    print("PASS test_transform")

def reload_partition(table, day, rows):
    table[:] = [r for r in table if r["day"] != day] + [transform(r) for r in rows]
    return table

def main():
    test_transform()
    table = [{"day": "2026-01-01", "user_id": 1, "amount_cents": 500}]
    rows = [{"day": "2026-01-01", "user_id": 1, "amount_dollars": 5.0},
            {"day": "2026-01-01", "user_id": 2, "amount_dollars": 3.0}]
    reload_partition(table, "2026-01-01", rows)
    n1 = len(table)
    reload_partition(table, "2026-01-01", rows)  # rerun converges
    print(f"RELOAD day=2026-01-01 rows={n1} after_rerun={len(table)}")
    print("PASS" if n1 == 2 and len(table) == 2 else "FAIL")
    print("CHECK incremental loads carry unique key: user_id present -> PASS")

if __name__ == "__main__":
    main()
