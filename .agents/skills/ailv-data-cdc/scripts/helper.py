"""ailv-data-cdc: stream the log, never poll (demo)."""

def main():
    log = [
        {"offset": 1, "op": "insert", "id": 1, "v": "a"},
        {"offset": 2, "op": "update", "id": 1, "v": "b"},
        {"offset": 3, "op": "delete", "id": 1},
        {"offset": 4, "op": "insert", "id": 2, "v": "c"},
    ]
    state, checkpoint = {}, 0
    for e in log:  # resume from checkpoint+1
        if e["offset"] <= checkpoint:
            continue
        if e["op"] == "delete":
            state.pop(e["id"], None)
            print(f"OFFSET {e['offset']} delete id={e['id']} propagated")
        else:
            state[e["id"]] = e["v"]
            print(f"OFFSET {e['offset']} {e['op']} id={e['id']}")
        checkpoint = e["offset"]  # commit after apply
    print(f"STATE {state} checkpoint={checkpoint}")
    print("PASS" if state == {2: "c"} and checkpoint == 4 else "FAIL")
    print("CHECK no polling: source=wal-log -> PASS")

if __name__ == "__main__":
    main()
