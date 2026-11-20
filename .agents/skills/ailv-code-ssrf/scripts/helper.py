"""ailv-code-ssrf helper: allowlist server-side fetches."""
from urllib.parse import urlparse

ALLOWLIST = {"api.example.com", "cdn.example.com"}
BLOCKED = {"169.254.169.254", "metadata.google.internal", "localhost", "127.0.0.1"}

URLS = [
    "https://api.example.com/data",
    "https://evil.example.net/steal",
    "http://169.254.169.254/latest/meta-data/",
    "https://cdn.example.com/img.png",
]


def verdict(url):
    host = urlparse(url).hostname or ""
    if host in BLOCKED:
        return "BLOCK internal/metadata"
    if host not in ALLOWLIST:
        return "BLOCK not allowlisted"
    return "ALLOW"


def main():
    for url in URLS:
        print(verdict(url) + " :: " + url)
    print("rule: timeouts + size caps on; prefer webhooks over server fetch")


if __name__ == "__main__":
    main()
