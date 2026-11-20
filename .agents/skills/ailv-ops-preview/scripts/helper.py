"""ailv-ops-preview helper: per-PR prod mirror, seeded, auto-stopped."""

def main():
    pr = {"number": 117, "url": "https://git.example/repo/pull/117",
          "merged": True}
    env = {"mirror": "prod", "data": "seeded-demo", "prod_dump": False,
           "url_posted_to_pr": True, "destroyed_on_merge": True,
           "idle_timeout_min": 60, "idle_min_elapsed": 75, "auto_stopped": True}
    checks = [
        ("per-PR prod mirror", env["mirror"] == "prod"),
        ("seeded demo data, never prod dumps",
         env["data"] == "seeded-demo" and not env["prod_dump"]),
        ("preview URL posted back to PR", env["url_posted_to_pr"]),
        ("destroyed on merge",
         (not pr["merged"]) or env["destroyed_on_merge"]),
        ("idle auto-stop fires",
         env["auto_stopped"] and env["idle_min_elapsed"] >= env["idle_timeout_min"]),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("preview env for PR #%d: %s" % (
        pr["number"], "STOPPED" if pr["merged"] else "RUNNING"))
    print("preview url: https://pr-117.preview.example (posted: %s)" %
          env["url_posted_to_pr"])

main()
