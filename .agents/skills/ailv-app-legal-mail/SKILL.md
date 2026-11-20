---
name: ailv-app-legal-mail
description: "One marketing mail without consent is spam under the law."
sources:
  - title: CAN-SPAM Act, 15 U.S.C. ch. 103
    url: https://www.law.cornell.edu/uscode/text/15/chapter-103
helper: scripts/helper.py
example: examples/output.md
---

# Mail by consent, not by list

`ailv-app-legal-mail` (Mail by consent, not by list): Treat order, delivery, and receipt mail as transactional (contract basis) — no consent needed, no marketing inside. Any marketing mail needs prior consent, names the seller with a working contact, and carries an opt-out that actually unsubscribes. Never move a transactional address onto a marketing list because it once bought something. Honor unsubscribes promptly and keep the suppression list forever.

## Checks

- order mail transactional-only, no marketing inside
- marketing needs prior consent plus a working opt-out
- buyer lists never merged into marketing lists
- suppression list kept indefinitely
