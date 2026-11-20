---
name: ailv-ops-secrets
description: "Committed secrets and manual rotation scatter copies that outlive every fix."
sources:
  - title: Vault docs
    url: https://developer.hashicorp.com/vault/docs
  - title: Mozilla SOPS
    url: https://github.com/getsops/sops
helper: scripts/helper.py
example: examples/output.md
---

# Vault-injected secrets, rotated automatically

`ailv-ops-secrets` (Vault-injected secrets, rotated automatically): Inject vault-backed secrets at runtime with RBAC — never commit secrets to repos or share one static value across environments. Rotate automatically on a schedule — no manual tickets, no copies in chat or env files. Audit every read; alert on reads from unexpected places. Seed the vault out of band: the first secret never travels through the systems it protects, and agents never hold root credentials.

## Checks

- runtime injection only, never committed
- rotation automatic, no manual tickets
- reads audited
