"""ailv-data-partition: prunable keys, no tiny files (demo)."""

def check_key(key, cardinality):
    if cardinality > 10000:
        return f"FAIL key={key} cardinality={cardinality} (tiny-file sprawl: use date)"
    return f"PASS key={key} cardinality={cardinality} prunable"

def main():
    print(check_key("day", 30))
    print(check_key("user_id", 2000000))
    files_mb = [0.2, 0.3, 0.1, 150.0]
    small = [f for f in files_mb if f < 10]
    print(f"FILES n={len(files_mb)} small={len(small)} -> "
          f"{'COMPACT scheduled' if small else 'ok'}")
    print("PASS" if small else "FAIL")

if __name__ == "__main__":
    main()
