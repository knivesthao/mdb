---
name: ailv-code-uploads
description: "Files through the app server bottleneck it; filenames lie; public buckets leak."
sources:
  - title: S3 presigned URLs
    url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html
helper: scripts/helper.py
example: examples/output.md
---

# Direct-to-storage, private by default

`ailv-code-uploads` (Direct-to-storage, private by default): Upload straight to storage with signed URLs — files never transit the app server. Trust MIME by content sniffing, never the filename; cap sizes at the edge. Scan asynchronously and quarantine on hit; serve everything private by default through signed URLs, never public buckets. Generate a unique key per upload — a same-key upload silently replaces the old object; bound URL lifetime to minutes, not days.

## Checks

- direct-to-storage signed URLs
- MIME sniffed, sizes capped
- private by default
- unique key per upload, short-lived URLs
