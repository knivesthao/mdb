---
name: ailv-data-retain
description: "Keep-forever drowns storage budgets and turns every breach into a GDPR incident."
sources:
  - title: GDPR full text
    url: https://gdpr-info.eu/
  - title: NIST SP 800-88 media sanitization
    url: https://csrc.nist.gov/pubs/sp/800/88/r1/final
helper: scripts/helper.py
example: examples/output.md
---

# Expire per policy, prove deletion

`ailv-data-retain` (Expire per policy, prove deletion): Expire or cold-store every dataset per written policy — cost and GDPR exposure both grow with keep-forever. PII gets the shortest retention and deletion on request with proof. Archive in open formats so cold data stays readable without the original cluster. Square erasure with immutable backups by key-per-subject shredding: destroying one subject's key deletes them from every backup holding it — deletion with proof, restores that still work.

## Checks

- policy per dataset, enforced
- PII deletable with proof
- open-format archives
