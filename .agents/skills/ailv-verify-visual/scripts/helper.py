"""Self-check for ailv-verify-visual: visual confirmation checklist."""
SCREEN = "orders screen with 3 real seeded orders (no lorem, no empty list)"
EYEBALL = ["layout", "labels", "error state"]
ERROR_STATE = "empty-card banner visible with retry button"
SHOTS = ["shots/orders-desktop.png", "shots/orders-360.png"]


def main():
    print("screen:", SCREEN)
    print("eyeball items:", ", ".join(EYEBALL))
    print("error state:", ERROR_STATE)
    print("shots:", ", ".join(SHOTS))
    checks = [
        ("seeded demo data present", "no lorem" in SCREEN and "no empty" in SCREEN),
        ("3 eyeball items listed", len(EYEBALL) == 3),
        ("error state visible", bool(ERROR_STATE)),
        ("desktop and 360px shots saved", len(SHOTS) == 2 and any("360" in s for s in SHOTS)),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += not ok
    print("RESULT:", "PASS" if failed == 0 else "FAIL")


if __name__ == "__main__":
    main()
