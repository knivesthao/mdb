"""ailv-code-fallback helper: shed load in criticality order under stress."""
import sys

# (feature, criticality: core first, nice-to-have last)
FEATURES = [
    ("checkout", "core"),
    ("order history", "standard"),
    ("recommendations", "shed-first"),
    ("polling/beacons", "shed-first"),
]


def decide(load_x):
    plan = []
    for name, tier in FEATURES:
        if tier == "core":
            plan.append((name, "serve"))
        elif tier == "standard":
            plan.append((name, "serve-stale-cache" if load_x >= 2 else "serve"))
        else:
            plan.append((name, "429+Retry-After" if load_x >= 2 else "serve"))
    return plan


def main():
    for load_x in (1, 2, 4):
        print(f"-- peak x{load_x} --")
        for name, action in decide(load_x):
            flag = "flag-gated" if action != "serve" and load_x >= 2 else "on"
            print(f"  {name}: {action} ({flag}, no deploy)")
    print("stress x4: core=serve, extras shed -> degraded mode holds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
