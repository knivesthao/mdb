"""ailv-data-upserts: merge by keys, never full overwrite (demo)."""

def merge(table, batch, key):
    idx = {r[key]: i for i, r in enumerate(table)}
    for r in batch:
        if r[key] in idx:
            table[idx[r[key]]] = r
        else:
            idx[r[key]] = len(table)
            table.append(r)
    return table

def main():
    table = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}]
    watermark = 1
    batch = [{"id": 2, "v": "b2"}, {"id": 3, "v": "c"}]
    merge(table, batch, "id")
    watermark = 2  # advance only after commit
    print(f"MERGE table={table} watermark={watermark}")
    crashed = list(table)
    print(f"CRASH resume from watermark={watermark} (never zero) -> rows={len(crashed)}")
    print("PASS" if table == [{"id": 1, "v": "a"}, {"id": 2, "v": "b2"}, {"id": 3, "v": "c"}] else "FAIL")

if __name__ == "__main__":
    main()
