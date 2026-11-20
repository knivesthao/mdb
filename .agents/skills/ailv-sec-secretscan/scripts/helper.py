"""ailv-sec-secretscan: revoke first, purge history, block at push."""
import re

PATTERNS = {
    "aws-key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "api-token": re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}['\"]?"),
}

PUSH_DIFF = [
    "db_host = 'localhost'",
    "aws_access = 'AKIAIOSFODNN7EXAMPLE'",
    "-----BEGIN RSA PRIVATE KEY-----",
    "api_key = 'sk-live-abc123XYZ789qrs'",
    "print('hello')",
]


def scan(lines):
    hits = []
    for i, line in enumerate(lines, 1):
        for name, rx in PATTERNS.items():
            if rx.search(line):
                hits.append((i, name, line.strip()[:40]))
    return hits


def main():
    hits = scan(PUSH_DIFF)
    print(f"push-time scan of {len(PUSH_DIFF)} lines: {len(hits)} hit(s)")
    for lineno, name, frag in hits:
        print(f"  line {lineno} [{name}]: {frag}...")
    if hits:
        print("verdict: BLOCK PUSH")
        print("response order: 1) revoke secret now 2) investigate 3) purge history+forks")
        print("              4) rotate everything the secret could reach")
    else:
        print("verdict: ALLOW PUSH")
    print("post-merge detection is backup, not the plan")


if __name__ == "__main__":
    main()
