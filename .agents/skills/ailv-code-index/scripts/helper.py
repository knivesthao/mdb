"""ailv-code-index helper: route a task description to the matched skills."""
import re

ALWAYS_ON = ["ailv-code-secure", "ailv-code-reuse", "ailv-code-token"]
RULES = [
    (r"interface|screen|component|page|landing", ["ailv-ui-index"]),
    (r"new service|new script|endpoint|cli", ["ailv-code-language", "ailv-code-shape"]),
    (r"organiz|new codebase|feature folder", ["ailv-code-group"]),
    (r"old codebase|inherit|legacy", ["ailv-code-legacy"]),
    (r"\bapi\b|public|form|beacon", ["ailv-code-ratelimit"]),
    (r"repeat|hot read", ["ailv-code-cache"]),
    (r"usage|count|analytics", ["ailv-code-track"]),
    (r"slow|heavy page", ["ailv-code-perf"]),
    (r"background|queue|worker|fan-out", ["ailv-code-async"]),
    (r"login|account|permission", ["ailv-code-auth"]),
    (r"sql inject|injection", ["ailv-code-injection"]),
    (r"secret|crypto|encrypt|hash", ["ailv-code-crypto"]),
]

DEMOS = [
    "Add a public API endpoint with a login form",
    "Speed up a slow endpoint with repeat traffic",
]


def match(task):
    found = list(ALWAYS_ON)
    low = task.lower()
    for pat, skills in RULES:
        if re.search(pat, low):
            for s in skills:
                if s not in found:
                    found.append(s)
    return found


def main():
    for task in DEMOS:
        print("task: " + task)
        print("skills: " + ", ".join(match(task)))
        print("fetch: one batched request, no duplicates")
    print("done: " + str(len(DEMOS)) + " tasks routed")


if __name__ == "__main__":
    main()
