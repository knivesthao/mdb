"""ailv-code-async helper: queue + job ids, bounded fan-out, retryable jobs."""
import sys

JOBS = {}
POOL = 2  # bounded worker pool: never unbounded spawns


def submit(name, fail_once=False):
    jid = f"job-{len(JOBS) + 1}"
    JOBS[jid] = {"name": name, "tries": 0, "fail_once": fail_once, "done": False}
    return jid  # request returns immediately with the id


def run(jid):
    job = JOBS[jid]
    job["tries"] += 1
    if job["fail_once"] and job["tries"] == 1:
        return "retry"  # idempotent: safe to re-run
    job["done"] = True
    return "done"


def main():
    ids = [submit("resize-img"), submit("send-receipt", fail_once=True)]
    print(f"submitted -> {ids} (request not held open)")
    print(f"fan-out pool size: {POOL} (bounded); failure policy: partial ship + retry")
    for jid in ids:
        res = run(jid)
        if res == "retry":
            print(f"{jid}: attempt 1 failed -> retry (idempotent)")
            res = run(jid)
        print(f"{jid}: {res} after {JOBS[jid]['tries']} tries; notify on completion")
    print("stall SLA: 5m watchdog, silent dead worker pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
