"""ailv-code-group helper: check files group by feature."""
FILES = [
    "checkout/checkout_routes.py",
    "checkout/checkout_models.py",
    "checkout/checkout_tests.py",
    "models/user.py",
    "controllers/user.py",
]

SHARED = {"contracts.py"}


def main():
    good = [f for f in FILES if "/" in f and f.split("/")[0] in f.split("/")[1]]
    scattered = [f for f in FILES if f not in good and f not in SHARED]
    for f in good:
        print("PASS grouped :: " + f)
    for f in scattered:
        print("FAIL scattered by layer :: " + f + " (move next to feature)")
    print("shared contracts: " + ", ".join(sorted(SHARED)))
    print("rule: follow the existing pattern over rewrites")


if __name__ == "__main__":
    main()
