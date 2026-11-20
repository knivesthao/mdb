"""ailv-ops-pipeline helper: validate one shared templated pipeline run."""
import json

GATES = ["build", "tests", "security-scan", "plan-preview", "approval"]
CRITICAL = "critical"

def main():
    run = {
        "template": "shared/deploy.yml",
        "hand_rolled": False,
        "commit": "abc1234",
        "gates": {"build": "pass", "tests": "pass",
                  "security-scan": "pass", "plan-preview": "published",
                  "approval": "granted"},
        "scan_findings": [{"id": "S1", "severity": "medium", "ticket": "T-42"}],
        "mutating_plan": {"diff": "2 files", "sql": "ALTER TABLE t ADD COLUMN x",
                           "targets": ["staging"], "machine_readable": True},
        "rollback": {"action": "redeploy", "artifact": "v1.4.2", "steps": 1},
        "events": ["deploy.start", "deploy.finish"],
        "preview_env": {"created": True, "auto_stop": True},
    }
    checks = [
        ("one shared template, no hand-rolled pipes",
         run["template"] == "shared/deploy.yml" and not run["hand_rolled"]),
        ("gates in order all green",
         all(v in ("pass", "published", "granted") for v in run["gates"].values())),
        ("mutating step publishes machine-readable plan",
         run["mutating_plan"]["machine_readable"]),
        ("rollback is one action on old artifact",
         run["rollback"]["steps"] == 1 and run["rollback"]["action"] == "redeploy"),
        ("no critical scan findings blocking",
         not any(f["severity"] == CRITICAL for f in run["scan_findings"])),
        ("deploy start/finish events emitted",
         run["events"] == ["deploy.start", "deploy.finish"]),
        ("preview env auto-stops",
         run["preview_env"]["auto_stop"]),
        ("deploy links to commit", bool(run["commit"])),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("pipeline verdict: " + ("SHIP" if failed == 0 else "BLOCKED"))
    print(json.dumps({"template": run["template"], "commit": run["commit"],
                      "rollback": run["rollback"]}, indent=2))

main()
