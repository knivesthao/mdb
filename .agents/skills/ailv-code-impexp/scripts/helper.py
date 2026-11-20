"""ailv-code-impexp helper: background-style bulk import, bad rows quarantined."""
import sys

CSV_ROWS = ["id,email,amount", "1,a@x.io,10", "2,NOT-AN-EMAIL,xx",
            "3,b@x.io,25", "4,,40"]  # demo file lines


def valid(row):
    parts = row.split(",")
    return len(parts) == 3 and "@" in parts[1] and parts[2].isdigit()


def main():
    batch, quarantined, done = 2, [], 0
    body = CSV_ROWS[1:]
    for i in range(0, len(body), batch):  # bounded batches, never whole table
        for row in body[i:i + batch]:
            done += 1
            if not valid(row):
                quarantined.append(row)
        print(f"progress: {done}/{len(body)} rows scanned")
    print(f"imported: {len(body) - len(quarantined)}, quarantined: {len(quarantined)}")
    for row in quarantined:
        print(f"  quarantine: {row}")
    print("notify: job complete + error report attached")
    return 0


if __name__ == "__main__":
    sys.exit(main())
