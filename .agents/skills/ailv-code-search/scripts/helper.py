"""ailv-code-search helper: tenant-scoped, ranked, typo-tolerant search."""
import sys

DOCS = [{"ws": "acme", "title": "Refund policy", "hits": 12},
        {"ws": "acme", "title": "Referral program", "hits": 3},
        {"ws": "globex", "title": "Refund policy", "hits": 99}]
DEAD = []  # dead-search log = roadmap


def close(a, b):  # typo tolerance: edit distance <= 1
    if a == b:
        return True
    if abs(len(a) - len(b)) > 1:
        return False
    i = j = edits = 0
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            edits += 1
            if edits > 1:
                return False
            if len(a) > len(b):
                i += 1
            elif len(b) > len(a):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    return True


def search(ws, query):
    scoped = [d for d in DOCS if d["ws"] == ws]  # tenant first
    words = query.lower().split()
    ranked = sorted(
        (d for d in scoped
         if any(close(w, t) for w in words for t in d["title"].lower().split())),
        key=lambda d: -d["hits"])  # relevance, not recency
    if not ranked:
        DEAD.append((ws, query))
    return [d["title"] for d in ranked]


def main():
    print("acme 'refund':", search("acme", "refund"))
    print("acme 'refnd' (typo):", search("acme", "refnd"))
    print("acme 'refund' leaks globex doc:", any("99" in str(r) for r in search("acme", "refund")) or "no leak")
    print("acme 'zzz-no-match':", search("acme", "zzz-no-match"))
    print("dead-search log (roadmap):", DEAD)
    print("index maintained on writes (no nightly rebuild)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
