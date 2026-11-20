"""ailv-code-language helper: typed-model validation, framework-first demo."""
from dataclasses import dataclass


@dataclass
class CreateUser:
    name: str
    age: int


def validate(raw):
    if not isinstance(raw.get("name"), str) or not raw["name"].strip():
        return None, "name must be a non-empty string"
    if not isinstance(raw.get("age"), int) or raw["age"] < 0:
        return None, "age must be a non-negative int"
    return CreateUser(name=raw["name"].strip(), age=raw["age"]), ""


def main():
    good = {"name": "Ada", "age": 30}
    bad = {"name": " ", "age": -1}
    user, _ = validate(good)
    print("valid input -> " + str(user))
    user2, err = validate(bad)
    print("invalid input -> user=" + str(user2) + " error=" + err)
    print("rule: one typed model drives validation; no hand-written type checks per field")


if __name__ == "__main__":
    main()
