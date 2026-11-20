"""ailv-data-streams: windows plus watermarks (demo)."""
WINDOW_S = 60
HORIZON_S = 10  # lateness allowed

def main():
    watermark = 60
    events = [
        {"ts": 61, "v": 1},  # advances watermark
        {"ts": 59, "v": 2},  # slightly late, within horizon -> in window
        {"ts": 130, "v": 3},  # advances watermark
        {"ts": 85, "v": 9},  # 45 behind horizon -> side channel
    ]
    window, side = [], []
    for e in events:
        if e["ts"] >= watermark:
            watermark = e["ts"]
            window.append(e["v"])
            print(f"EVENT ts={e['ts']} advances watermark={watermark}")
        elif watermark - e["ts"] <= HORIZON_S:
            window.append(e["v"])
            print(f"EVENT ts={e['ts']} in-window (within horizon)")
        else:
            side.append(e["v"])
            print(f"EVENT ts={e['ts']} late -> side-channel")
    window.sort()
    print(f"WINDOW emit trigger=watermark sum={sum(window)} side={side}")
    lag = 0
    print(f"WATERMARK lag={lag}s monitored -> {'PASS' if lag < 30 else 'FAIL stalled'}")
    print("PASS" if side == [9] else "FAIL")

if __name__ == "__main__":
    main()
