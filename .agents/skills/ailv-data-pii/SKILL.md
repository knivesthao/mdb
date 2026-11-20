---
name: ailv-data-pii
description: "Retention rules on unlabeled data are theater; the PII lives in note_2."
sources:
  - title: NIST SP 800-122 PII guide
    url: https://csrc.nist.gov/pubs/sp/800/122/final
  - title: GDPR full text
    url: https://gdpr-info.eu/
helper: scripts/helper.py
example: examples/output.md
---

# Find PII before you policy it

`ailv-data-pii` (Find PII before you policy it): Classify before retaining: scan text fields, webhook payloads, and new columns for personal data on a schedule — PII hides in free text and oddly named columns. Label what you find at the source; retention and erasure act on labels, never on guesses. Quarantine unlabeled new sources until classified. Re-scan when producers change shape.

## Checks

- scheduled scans of text and new columns
- retention acts on labels
- unlabeled sources quarantined
