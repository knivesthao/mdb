"""ailv-code-crypto helper: scan demo code for crypto mistakes."""
import re
from datetime import datetime, timedelta, timezone

DEMO_LINES = [
    "cipher = xor_encrypt(data, key)  # hand-rolled",
    "API_KEY = 'sk-live-12345'",
    "token = secrets.token_urlsafe(32)",
    "password = bcrypt.hashpw(pw, salt)",
]


def scan(lines):
    findings = []
    for i, line in enumerate(lines, 1):
        if re.search(r"xor_encrypt|rot13|custom_cipher|md5.*password", line, re.I):
            findings.append("line " + str(i) + ": hand-rolled cipher")
        if re.search(r"sk-live|AKIA|password\s*=\s*['\"]", line):
            findings.append("line " + str(i) + ": possible secret in code")
    return findings


def main():
    for f in scan(DEMO_LINES) or ["no findings"]:
        print(f)
    issued = datetime.now(timezone.utc)
    expiry = issued + timedelta(hours=1)
    print("token issued: " + issued.isoformat(timespec="seconds"))
    print("token expires: " + expiry.isoformat(timespec="seconds") + " (scoped: read-only)")
    print("rule: platform crypto only; secrets in env; tokens expire and are scoped")


if __name__ == "__main__":
    main()
