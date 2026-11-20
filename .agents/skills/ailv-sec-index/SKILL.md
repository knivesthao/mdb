---
name: ailv-sec-index
description: "Vulns without owners sit for months — map first, scan-and-sit never."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Security ops: pick sec skills

`ailv-sec-index` (Security ops: pick sec skills): Your security-ops skills each do one job — never read them all. Known vulnerabilities → ailv-sec-vuln. Enterprise login, MFA, break-glass → ailv-sec-sso. App login basics → ailv-code-auth. Image and dependency scans → ailv-sec-scan. Leaked secrets → ailv-sec-secretscan. Sessions and tokens → ailv-sec-session. SIEM → ailv-sec-siem. WAF → ailv-sec-waf. Anomaly detection → ailv-sec-anomaly. Breach runbooks → ailv-sec-runbooks. Patching → ailv-sec-patch. Compliance evidence → ailv-sec-compliance. Hardening the code itself (validation, crypto, auth, sessions) → the OWASP deep-dives from the bank map you started with. Humans verify finding counts and drill logs — never the runbook text. Skip everything else.

## Checks

- only matched sec skills are read
- app basics stay in ailv-code-auth
