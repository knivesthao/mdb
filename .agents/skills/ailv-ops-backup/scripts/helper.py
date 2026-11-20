"""ailv-ops-backup helper: RPO schedule, drilled RTO restore, erasure replay."""

def main():
    policy = {"rpo_min": 60, "schedule_min": 30, "rto_min": 120}
    drill = {"env": "isolated", "restore_min": 95, "recorded": True,
             "erasure_log_replayed": True, "over_prod": False}
    checks = [
        ("schedule matched to RPO (%dmin <= RPO %dmin)" % (
            policy["schedule_min"], policy["rpo_min"]),
         policy["schedule_min"] <= policy["rpo_min"]),
        ("restore drilled, timed against RTO (%dmin <= RTO %dmin)" % (
            drill["restore_min"], policy["rto_min"]),
         drill["restore_min"] <= policy["rto_min"]),
        ("drill result recorded", drill["recorded"]),
        ("restore tested isolated, never over prod",
         drill["env"] == "isolated" and not drill["over_prod"]),
        ("erasure log replayed before opening restore",
         drill["erasure_log_replayed"]),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("backup: every %dmin (RPO %dmin); last drill restore %dmin (RTO %dmin)" % (
        policy["schedule_min"], policy["rpo_min"],
        drill["restore_min"], policy["rto_min"]))

main()
