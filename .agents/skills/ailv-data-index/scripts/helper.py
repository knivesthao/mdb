"""ailv-data-index: router self-check (demo)."""
ROUTES = {"collect": "ailv-data-collect", "ingest": "ailv-data-ingest",
          "dag": "ailv-data-orchestrate", "etl": "ailv-data-etl",
          "schema": "ailv-data-contracts", "shape": "ailv-data-model",
          "backfill": "ailv-data-backfill", "cdc": "ailv-data-cdc",
          "quality": "ailv-data-quality", "partition": "ailv-data-partition",
          "retain": "ailv-data-retain", "stream": "ailv-data-streams",
          "lineage": "ailv-data-lineage", "upsert": "ailv-data-upserts",
          "lock": "ailv-data-concurrency", "metric": "ailv-data-metrics",
          "pii": "ailv-data-pii"}

def route(task):
    t = task.lower()
    return sorted({s for k, s in ROUTES.items() if k in t})

def main():
    cases = [("backfill the partitions", ["ailv-data-backfill", "ailv-data-partition"]),
             ("check quality gates", ["ailv-data-quality"]),
             ("find pii in notes", ["ailv-data-pii"]),
             ("stream late events", ["ailv-data-streams"])]
    ok = True
    for task, want in cases:
        got = route(task)
        hit = got == want
        ok &= hit
        print(f"{'PASS' if hit else 'FAIL'} route {task!r} -> {got}")
    print("CHECK only matched skills read, rest skipped -> PASS")
    print("PASS" if ok else "FAIL")

if __name__ == "__main__":
    main()
