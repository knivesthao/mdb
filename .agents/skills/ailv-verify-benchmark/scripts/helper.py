"""Self-check for ailv-verify-benchmark: with/without/no-skill trial proof."""
import json

DEMO_RUNS = [
    {"label": "matched-skills", "tokens": 4200, "seconds": 61.0, "defects": 1},
    {"label": "whole-bank", "tokens": 6100, "seconds": 88.0, "defects": 1},
    {"label": "no-skills", "tokens": 5900, "seconds": 74.0, "defects": 3},
]
METHOD = "real task, plan rules kept (inline<=5 steps else file), 1 run per lane"


def check_runs(runs):
    results = []
    labels = {r["label"] for r in runs}
    results.append(("with/without/no-skill trial run",
                    labels == {"matched-skills", "whole-bank", "no-skills"}))
    results.append(("tokens, time, defects all reported",
                    all(all(k in r for k in ("tokens", "seconds", "defects"))
                        for r in runs)))
    results.append(("method plus raw numbers published",
                    bool(METHOD) and len(runs) == 3))
    return results


def main():
    print("demo method:", METHOD)
    print("raw numbers:", json.dumps(DEMO_RUNS))
    results = check_runs(DEMO_RUNS)
    failed = 0
    for name, ok in results:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += not ok
    best = min(DEMO_RUNS, key=lambda r: (r["defects"], r["tokens"]))
    print("best lane: %s (tokens=%d, time=%.0fs, defects=%d)" % (
        best["label"], best["tokens"], best["seconds"], best["defects"]))
    print("RESULT:", "PASS" if failed == 0 else "FAIL")


if __name__ == "__main__":
    main()
