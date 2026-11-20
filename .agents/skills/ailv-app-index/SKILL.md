---
name: ailv-app-index
description: "Billing, roles, and invites repeat in every system — map first, build the rest from shape."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Product features: pick product skills

`ailv-app-index` (Product features: pick product skills): Your product skills each do one job — never read them all. Billing and plans → ailv-code-billing. Team roles, admin console, impersonation → ailv-code-rbac. Invites and membership → ailv-code-invites. Notifications → ailv-code-notify. Search → ailv-code-search. Uploads → ailv-code-uploads. Audit trail → ailv-code-auditlog. Outgoing webhooks → ailv-code-webhooks. Customer API keys → ailv-code-apikeys. Flags and entitlements → ailv-code-flags. Bulk moves → ailv-code-impexp. Login and sessions → ailv-code-auth. Selling anything — privacy, terms, card scope, tax → ailv-app-legal. Skip everything else. Meter new product work with ailv-code-track.

## Checks

- only matched product skills are read
- auth always via ailv-code-auth
- new product work metered with ailv-code-track
