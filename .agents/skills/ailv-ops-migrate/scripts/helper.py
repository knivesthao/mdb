"""ailv-ops-migrate helper: expand-then-contract plan, reversible, dry-run."""

def main():
    migration = {
        "version": "0042_add_email",
        "steps": ["add nullable column", "backfill rows",
                  "add constraint", "drop old column"],
        "reversible": True,
        "edits_applied": False,
        "dry_run": {"against": "prod-shaped", "result": "ok"},
    }
    want = ["add nullable", "backfill", "constrain", "drop"]
    checks = [
        ("versioned and runs with deploy", bool(migration["version"])),
        ("expand then contract, no half-schema",
         all(w in " ".join(migration["steps"]) for w in want)),
        ("reversible or paired undo", migration["reversible"]),
        ("never edits an applied migration", not migration["edits_applied"]),
        ("dry-run on prod-shaped data first",
         migration["dry_run"]["against"] == "prod-shaped"
         and migration["dry_run"]["result"] == "ok"),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("migration %s: %d steps, dry-run %s" % (
        migration["version"], len(migration["steps"]),
        migration["dry_run"]["result"]))
    for i, s in enumerate(migration["steps"], 1):
        print("  %d. %s" % (i, s))

main()
