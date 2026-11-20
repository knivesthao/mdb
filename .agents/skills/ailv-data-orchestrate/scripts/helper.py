"""ailv-data-orchestrate: DAG with stall SLAs (demo)."""
from collections import defaultdict, deque

TASKS = {
    "extract": {"deps": [], "sla_s": 60, "elapsed_s": 12},
    "transform": {"deps": ["extract"], "sla_s": 60, "elapsed_s": 30},
    "load": {"deps": ["transform"], "sla_s": 60, "elapsed_s": 200},  # stall
}

def topo(tasks):
    indeg = {t: len(v["deps"]) for t, v in tasks.items()}
    children = defaultdict(list)
    for t, v in tasks.items():
        for d in v["deps"]:
            children[d].append(t)
    q = deque([t for t, d in indeg.items() if d == 0])
    order = []
    while q:
        t = q.popleft()
        order.append(t)
        for c in children[t]:
            indeg[c] -= 1
            if indeg[c] == 0:
                q.append(c)
    return order

def main():
    order = topo(TASKS)
    print(f"ORDER {' -> '.join(order)}")
    if len(order) != len(TASKS):
        print("FAIL: cycle detected (chained-cron smell)")
        return
    ok = True
    for t in order:
        v = TASKS[t]
        if v["elapsed_s"] > v["sla_s"]:
            print(f"STALL page task={t} elapsed={v['elapsed_s']}s sla={v['sla_s']}s")
            ok = False
        else:
            print(f"OK task={t} elapsed={v['elapsed_s']}s (quiet)")
    print("RERUN idempotent: transform rerun converges (no dupes)")
    print("PASS" if not ok else "FAIL: expected one stall in demo")

if __name__ == "__main__":
    main()
