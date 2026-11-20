---
name: ailv-code-sqlmodel
description: "Table models skip init validation and hide columns from checkers; three measured rules, fetched only on a SQLModel stack."
---

# SQLModel quirks, gated

`ailv-code-sqlmodel` (SQLModel quirks, pay-as-you-go): Fetch only when the stack mentions SQLModel — never by default. Three measured rules. Table models skip `__init__` validation: never assert Pydantic-style validation on construction; test invalid input through `Model.model_validate({...})` with a dict. Metaclass columns are invisible to static analysis: `order_by`/`desc` take `# type: ignore` on the first attempt, never `__table__.c` workarounds. One model serves as table and validator: keep column config on the model, never a parallel schema for the same shape.

## Checks

- fetched only when the stack says SQLModel
- no validation asserted on table-model construction
- order_by ignored on first attempt, no workaround loops
- invalid-input tests use model_validate dict form
