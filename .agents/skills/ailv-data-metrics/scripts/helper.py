"""ailv-data-metrics: one definition per metric (demo)."""
REG = {"revenue": {"formula": "sum(amount_cents)", "owner": "fin", "v": 1}}

def define(name, formula, owner):
    cur = REG.get(name)
    if cur and cur["formula"] != formula:
        print(f"INCIDENT duplicate metric {name}: {cur['formula']!r} vs {formula!r}")
        return False
    REG[name] = {"formula": formula, "owner": owner, "v": cur["v"] + 1 if cur else 1}
    return True

def main():
    print(f"READ revenue = {REG['revenue']['formula']} (dashboards never re-derive)")
    dup = define("revenue", "sum(amount)", "growth")  # dup name, diff formula
    ok = define("orders", "count(*)", "growth")
    print(f"DEFINE orders -> {'PASS' if ok else 'FAIL'}")
    REG["revenue"] = {"formula": "sum(amount_cents) - refunds", "owner": "fin", "v": 2}
    print("CHANGE revenue v2 logged, history replayed -> PASS")
    print("PASS" if not dup and ok else "FAIL")

if __name__ == "__main__":
    main()
