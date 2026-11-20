"""ailv-code-docs: docs agents can read self-check (demo)."""
DOC = {"id": "api.orders.v2", "shape": ["inputs", "outputs", "errors"],
       "generated_from": "models/order.py", "ends_with_check": True,
       "version": "v2", "signed": True}

def main():
    checks = [
        ("reference generated from source", bool(DOC.get("generated_from"))),
        ("uniform shape + stable id", DOC["shape"] == ["inputs", "outputs", "errors"] and bool(DOC.get("id"))),
        ("ends in executable check", DOC["ends_with_check"]),
        ("versioned and signed", bool(DOC.get("version")) and DOC["signed"]),
    ]
    ok = True
    for name, hit in checks:
        ok &= hit
        print(f"{'PASS' if hit else 'FAIL'} {name}")
    print("PASS" if ok else "FAIL")

if __name__ == "__main__":
    main()
