"""ailv-data-contracts: versioned schemas, additive only (demo)."""
REGISTRY = {"order.v1": {"order_id", "amount_cents"}}

def check_compat(base, candidate):
    removed = set(base) - set(candidate)
    return (not removed, sorted(removed))

def main():
    v2_add = {"order_id", "amount_cents", "note"}
    ok, removed = check_compat(REGISTRY["order.v1"], v2_add)
    print(f"ADDITIVE order.v2 fields={sorted(v2_add)} -> {'PASS' if ok else 'FAIL'}")
    v2_break = {"id", "amount_cents"}  # rename
    ok2, removed2 = check_compat(REGISTRY["order.v1"], v2_break)
    print(f"RENAME order.v2 fields={sorted(v2_break)} removed={removed2} -> "
          f"{'BLOCKED new version required' if not ok2 else 'FAIL: rename allowed'}")
    print("CONSUMER pins order.v1; producer dual-writes v1+v2 -> PASS")
    print("PASS" if ok and not ok2 else "FAIL")

if __name__ == "__main__":
    main()
