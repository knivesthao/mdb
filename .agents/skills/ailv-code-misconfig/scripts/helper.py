"""ailv-code-misconfig helper: verify production settings are safe."""
CONFIG = {
    "DEBUG": False,
    "TRACE": False,
    "HSTS": True,
    "CSP": "default-src 'self'",
    "CORS_ORIGINS": ["https://app.example.com"],
    "ADMIN_PASSWORD": "**** (no default)",
    "ERROR_PAGE": "generic",
}


def check(cfg):
    findings = []
    if cfg.get("DEBUG") or cfg.get("TRACE"):
        findings.append("FAIL debug/trace must be off in production")
    else:
        findings.append("PASS debug off in production")
    if not cfg.get("HSTS") or not cfg.get("CSP"):
        findings.append("FAIL security headers missing")
    else:
        findings.append("PASS security headers set")
    origins = cfg.get("CORS_ORIGINS", [])
    if "*" in origins:
        findings.append("FAIL CORS wildcard")
    else:
        findings.append("PASS CORS allowlist (no wildcard)")
    if cfg.get("ADMIN_PASSWORD") in ("admin", "password", "changeme"):
        findings.append("FAIL default password")
    else:
        findings.append("PASS no default passwords")
    return findings


def main():
    for k, v in CONFIG.items():
        print(k + " = " + str(v))
    for line in check(CONFIG):
        print(line)


if __name__ == "__main__":
    main()
