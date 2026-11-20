---
name: ailv-code-injection
description: "Injection is input treated as instructions; parameters keep input as data."
sources:
  - title: OWASP SQL Injection Prevention
    url: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
helper: scripts/helper.py
example: examples/output.md
---

# Input stays data

`ailv-code-injection` (Input stays data): Never build queries, commands, or markup by gluing strings around user input. Database reads go through the ORM (parameterized queries, never interpolation). Templates auto-escape HTML — never mark user content safe. OS commands, LDAP, and XPath get the same rule: parameters, never concatenation.

## Checks

- no string-built queries or commands
- user HTML never marked safe
- ORM or parameters everywhere
