"""ailv-code-cache helper: one get/set/invalidate interface, swappable store."""
import hashlib
import time

store = {}


def get(key):
    return store.get(key)


def set(key, value):
    store[key] = value


def invalidate(key):
    store.pop(key, None)


def etag(body):
    return hashlib.md5(body.encode()).hexdigest()[:8]


def main():
    set("report:7d", "computed-answer")
    print("get hit: " + str(get("report:7d")))
    print("etag: " + etag("computed-answer") + " -> 304 Not Modified on match")
    invalidate("report:7d")
    print("after write invalidate, get: " + str(get("report:7d")))
    print("rule: never cache user secrets; invalidate on write, not timer alone")


if __name__ == "__main__":
    main()
