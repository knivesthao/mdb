---
name: ailv-sec-vuln
description: "Scan-and-sit is the failure mode — findings without owners and SLAs age into breaches."
sources:
  - title: NVD
    url: https://nvd.nist.gov/
  - title: CVSS
    url: https://www.first.org/cvss/
helper: scripts/helper.py
example: examples/output.md
---

# Every finding owned with a deadline

`ailv-sec-vuln` (Every finding owned with a deadline): Scan continuously and rank by exploitability, not by count: every finding gets an owner and a deadline scaled to reachability. Block the build on critical findings in CI and fail closed when the scanner errors — fail-open ships the vuln. Rescan to close; a finding without a retest stays open. Track mean-time-to-remediate per severity; scan-and-sit is the failure mode.

## Checks

- every finding owned with a deadline
- CI fails closed on scanner errors
- closure requires retest
