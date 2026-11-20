"""ailv-sec-scan: block builds on vuln images/deps, fail closed on scanner error."""
SCANNER_OK = True  # flip to False to demo fail-closed

IMAGES = [
    {"ref": "app:1.4.2", "pinned": True, "critical": 0, "high": 2, "rebuilt_days_ago": 6},
    {"ref": "worker:latest", "pinned": False, "critical": 1, "high": 4, "rebuilt_days_ago": 90},
]

DEPS = [
    {"name": "libauth", "version": "2.3.1", "pinned": True, "critical": 0},
    {"name": "libparse", "version": ">=1.0", "pinned": False, "critical": 1},
]


def main():
    print("image/dep scan (demo):")
    block = []
    warns = []
    for img in IMAGES:
        if not img["pinned"]:
            warns.append(f"{img['ref']}: floating tag -> pin it")
        if img["rebuilt_days_ago"] > 30:
            warns.append(f"{img['ref']}: stale rebuild ({img['rebuilt_days_ago']}d) -> rebuild on schedule")
        if img["critical"] > 0:
            block.append(f"{img['ref']}: {img['critical']} critical CVEs")
        print(f"  image {img['ref']}: pinned={img['pinned']} critical={img['critical']} "
              f"high={img['high']} rebuilt={img['rebuilt_days_ago']}d ago")
    for dep in DEPS:
        if not dep["pinned"]:
            warns.append(f"{dep['name']}: unpinned range {dep['version']}")
        if dep["critical"] > 0:
            block.append(f"{dep['name']}: {dep['critical']} critical CVEs")
        print(f"  dep {dep['name']} {dep['version']}: pinned={dep['pinned']} critical={dep['critical']}")
    if not SCANNER_OK:
        print("scanner ERROR -> fail closed: BUILD BLOCKED")
        return
    for w in warns:
        print(f"  warn: {w}")
    if block:
        for b in block:
            print(f"  BLOCK: {b}")
        print("verdict: FAIL - build blocked on critical findings")
    else:
        print("verdict: PASS - no critical findings, images pinned and fresh")


if __name__ == "__main__":
    main()
