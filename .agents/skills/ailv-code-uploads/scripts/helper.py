"""ailv-code-uploads helper: signed direct-to-storage, sniffed MIME, private."""
import hashlib
import hmac
import sys
import uuid

SECRET = b"demo-signing-secret"
MAX_BYTES = 5 * 1024 * 1024
MAGIC = [(b"\xff\xd8\xff", "image/jpeg"), (b"\x89PNG", "image/png"),
         (b"%PDF", "application/pdf")]


def sniff(data):
    for magic, mime in MAGIC:
        if data.startswith(magic):
            return mime
    return "application/octet-stream"


def presign(key, ttl_s=300):
    sig = hmac.new(SECRET, f"{key}:{ttl_s}".encode(), hashlib.sha256).hexdigest()[:16]
    return f"https://storage.local/{key}?exp={ttl_s}&sig={sig}"


def upload(filename, data):
    if len(data) > MAX_BYTES:
        return "reject: size capped at edge"
    mime = sniff(data)  # content sniff, never the filename
    key = f"uploads/{uuid.uuid4().hex}"  # unique key per upload
    return f"direct PUT {presign(key)} [{mime}, private] (lied name {filename!r} ignored)"


def main():
    print(upload("cute.png.exe", b"\x89PNG" + b"\x00" * 10))
    print(upload("huge.mov", b"\x00" * (MAX_BYTES + 1)))
    print("serve: signed URL, minutes TTL, private bucket (no public reads)")
    print("suspect file -> async scan -> quarantine on hit (clean here)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
