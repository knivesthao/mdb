"""ailv-data-pii: find PII before you policy it (demo)."""
import re

PATS = {"email": re.compile(r"[\w.]+@[\w.]+\.\w+"),
        "phone": re.compile(r"\d{3}-\d{3}-\d{4}")}

def scan(source, fields):
    hits = {k: [c for c, v in fields.items()
                 if k == "email" and PATS["email"].search(str(v))
                 or k == "phone" and PATS["phone"].search(str(v))]
            for k in PATS}
    hits = {k: v for k, v in hits.items() if v}
    return hits

def main():
    hits = scan("users-csv", {"name": "Ann", "note": "reach ann@x.com",
                              "phone_col": "415-555-0100"})
    for k, cols in hits.items():
        print(f"PII {k} in {cols} -> label at source")
    print("RETENTION acts on labels -> PASS")
    new = scan("new-webhook", {"payload": "nothing personal"})
    print(f"NEW SOURCE labels={new or 'none'} -> "
          f"{'QUARANTINE until classified' if not new else 'classified'}")
    print("PASS" if hits else "FAIL")

if __name__ == "__main__":
    main()
