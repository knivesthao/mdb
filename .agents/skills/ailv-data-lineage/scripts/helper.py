"""ailv-data-lineage: trace any number to its origin (demo)."""
RUNS = [
    {"run": "r1", "source": "orders-db", "transform": "normalize",
     "output": "marts.orders", "ts": "2026-01-01T00:00:00Z"},
    {"run": "r2", "source": "marts.orders", "transform": "revenue_sum",
     "output": "dash.revenue", "ts": "2026-01-01T01:00:00Z"},
]

def trace(dataset):
    chain = []
    cur = dataset
    for _ in range(10):
        hit = next((r for r in reversed(RUNS) if r["output"] == cur), None)
        if not hit:
            break
        chain.append(hit)
        cur = hit["source"]
    return list(reversed(chain))

def main():
    chain = trace("dash.revenue")
    for r in chain:
        print(f"RUN {r['run']}: {r['source']} --[{r['transform']}]--> {r['output']}")
    print(f"ORIGIN dash.revenue = {chain[0]['source'] if chain else '?'} (one lookup)")
    print("PASS" if len(chain) == 2 and chain[0]["source"] == "orders-db" else "FAIL")

if __name__ == "__main__":
    main()
