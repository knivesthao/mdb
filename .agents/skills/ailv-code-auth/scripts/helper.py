"""ailv-code-auth helper: default-deny permission check demo."""
import hashlib
import hmac

PERMS = {
    "admin": {"read", "write", "delete"},
    "editor": {"read", "write"},
    "viewer": {"read"},
}

USERS = {"ada": "admin", "bob": "viewer"}


def hash_password(password, salt="demo-salt"):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 1000).hex()


def can(user, action):
    role = USERS.get(user)
    if role is None:
        return False
    return action in PERMS.get(role, set())


def main():
    print("password hash (bcrypt in real code): " + hash_password("s3cret")[:16] + "...")
    cases = [("ada", "delete"), ("bob", "delete"), ("bob", "read"), ("ghost", "read")]
    for user, action in cases:
        print(user + " may " + action + ": " + ("ALLOW" if can(user, action) else "DENY"))
    print("rule: signed-cookie sessions; bcrypt passwords; per-action check, default deny")


if __name__ == "__main__":
    main()
