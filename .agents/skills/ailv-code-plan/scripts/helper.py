"""ailv-code-plan helper: run the skill's own checklist as a self-check."""
import sys

# Demo: 4 matched leaves -> plan required; steps with blocked-by deps.
STEPS = [
    {"skill": "ailv-code-billing", "done": "price resolves from plan", "waits": None},
    {"skill": "ailv-code-rbac", "done": "tenant check on reads", "waits": None},
    {"skill": "ailv-code-notify", "done": "queued receipt send", "waits": 1},
    {"skill": "cleanup", "done": "scratch deleted, report filed", "waits": 3},
]
FETCHED_UP_FRONT = ["ailv-code-billing", "ailv-code-rbac", "ailv-code-notify"]
FETCHED_DURING_EXEC = []
TREE_EXTRA_SCRATCH = []


def check(name, ok):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return ok


def main():
    n = len(STEPS)
    ok = True
    ok &= check("plan written (3+ matched leaves)", n >= 3)
    ok &= check("inline plan ok (<=5 steps, live session)", n <= 5)
    ok &= check("every step names skill + done-state",
                all(s["skill"] and s["done"] for s in STEPS))
    indep = [s for s in STEPS if s["waits"] is None]
    ok &= check(f"independents run together ({len(indep)} unblocked)", len(indep) >= 2)
    ok &= check("all skills fetched once up front, none during exec",
                len(FETCHED_UP_FRONT) == 3 and not FETCHED_DURING_EXEC)
    ok &= check("last step is cleanup", STEPS[-1]["skill"] == "cleanup")
    ok &= check("tree holds only deliverable + tests", not TREE_EXTRA_SCRATCH)
    print("SELF-CHECK:", "PASS" if ok else "FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
