"""ailv-ops-index helper: route ops work to exactly the skill that owns it."""

ROUTES = {
    "build-test-deploy gates": "ailv-ops-pipeline",
    "logs metrics traces paging": "ailv-ops-observe",
    "preview env": "ailv-ops-preview",
    "migration": "ailv-ops-migrate",
    "rollout canary": "ailv-ops-rollout",
    "secrets at runtime": "ailv-ops-secrets",
    "backup restore drill": "ailv-ops-backup",
    "infra as code": "ailv-ops-iac",
    "autoscaling": "ailv-ops-scale",
    "health probes": "ailv-ops-probes",
    "rotation postmortem": "ailv-ops-oncall",
    "destructive op failing actor": "ailv-ops-safety",
    "cut a release": "ailv-ops-release",
    "two agents one deploy": "ailv-ops-coordinate",
}

def route(task):
    task = task.lower()
    for key, skill in ROUTES.items():
        if any(w in task for w in key.split()):
            return skill
    return None

def main():
    demo = {"migration": "ailv-ops-migrate",
            "canary rollout is stuck": "ailv-ops-rollout",
            "rotate the db password": "ailv-ops-secrets",
            "preview env for my PR": "ailv-ops-preview"}
    failed = 0
    for task, want in demo.items():
        got = route(task)
        ok = got == want
        print(("PASS" if ok else "FAIL") + ": '%s' -> %s" % (task, got))
        failed += 0 if ok else 1
    print(("PASS" if len(ROUTES) == 14 else "FAIL") +
          ": index covers 14 ops skills (%d)" % len(ROUTES))
    failed += 0 if len(ROUTES) == 14 else 1
    print("index verdict: " +
          ("ONLY-MATCHED-READ" if failed == 0 else "MISROUTED"))

main()
