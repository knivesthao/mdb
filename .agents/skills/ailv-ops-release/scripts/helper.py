"""ailv-ops-release helper: validate one batched, versioned release."""
import re

def bump(version, kind):
    major, minor, patch = (int(x) for x in version.split("."))
    if kind == "patch":
        patch += 1
    elif kind == "minor":
        minor += 1
        patch = 0
    elif kind == "major":
        major += 1
        minor = 0
        patch = 0
    return "%d.%d.%d" % (major, minor, patch)

def main():
    current, kind = "1.4.2", "minor"  # demo: new skill added
    pending_changes = ["add preview auto-stop", "fix probe timeout",
                       "docs touch-up", "refactor helper"]
    releases_today, hotfix = 0, False
    nxt = bump(current, kind)
    assert re.match(r"^\d+\.\d+\.\d+$", nxt)
    artifacts = {"changelog": nxt, "signatures": nxt, "feed": nxt,
                 "bank_version": nxt}
    checks = [
        ("batched: one version for %d changes" % len(pending_changes),
         len(pending_changes) > 1),
        ("semver bump %s -> %s (%s)" % (current, nxt, kind),
         nxt == "1.5.0"),
        ("changelog, signatures, feed, version move together",
         len(set(artifacts.values())) == 1),
        ("no second release today (or hotfix only)",
         releases_today == 0 or hotfix),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("release: %s (changes: %d)" % (nxt, len(pending_changes)))
    for c in pending_changes:
        print("  - " + c)

main()
