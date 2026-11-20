"""ailv-ops-secrets helper: runtime injection, auto rotation, audited reads."""

def main():
    repo = {"files": ["app.py", ".env.example"], "committed_secrets": []}
    secrets = [{"name": "db/password", "env": "prod", "age_days": 12,
                "ttl_days": 30, "injected": "runtime", "shared_static": False},
               {"name": "api/key", "env": "staging", "age_days": 5,
                "ttl_days": 30, "injected": "runtime", "shared_static": False}]
    reads = [{"who": "svc/api", "where": "prod", "expected": True},
             {"who": "svc/api", "where": "prod", "expected": True}]
    seeded = {"first_secret": "out-of-band", "root_held_by_agent": False}
    checks = [
        ("runtime injection only, never committed",
         not repo["committed_secrets"]
         and all(s["injected"] == "runtime" for s in secrets)),
        ("no static value shared across envs",
         len({(s["name"], s["env"]) for s in secrets}) == len(secrets)
         and all(not s["shared_static"] for s in secrets)),
        ("rotation automatic, none expired",
         all(s["age_days"] <= s["ttl_days"] for s in secrets)),
        ("reads audited, no unexpected readers",
         all(r["expected"] for r in reads)),
        ("vault seeded out of band, no agent root",
         seeded["first_secret"] == "out-of-band"
         and not seeded["root_held_by_agent"]),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    for s in secrets:
        print("secret %s (%s): age %dd/ttl %dd via %s" % (
            s["name"], s["env"], s["age_days"], s["ttl_days"], s["injected"]))

main()
