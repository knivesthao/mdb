---
name: ailv-data-quality
description: "Row counts pass plausible-but-wrong data; the bad numbers ship to every dashboard."
sources:
  - title: Great Expectations docs
    url: https://docs.greatexpectations.io/docs/oss/overview
helper: scripts/helper.py
example: examples/output.md
---

# Gate promotion on signals, not row counts

`ailv-data-quality` (Gate promotion on signals, not row counts): Gate every promotion on freshness, nulls, volume, and distribution — row counts alone pass plausible-but-wrong data. Failing checks block the pipeline and page the dataset owner, with the offending sample attached. Track quality history per dataset; page only on shifts that name an owner and an action — alert fatigue trains teams to ignore every page, including real ones. Keep leniency explicit: any allow-X-percent threshold is named and owned, never a quiet default — a lenient gate passes plausible-but-wrong data by design.

## Checks

- multi-signal gates, not row counts
- failures block with samples
- quality history tracked
