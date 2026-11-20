"""Reasoning-display router demo: panel events -> visible shape. Stdlib only."""

SHAPES = {
    "routine step": "one line, no report",
    "decision": "decision plus evidence, never the choosing",
    "done work": "what changed plus proof it ran",
    "full trace": "local log only, excluded from context",
    "blocked or failed": "exactly what is needed to unblock, nothing else",
}

for event, shape in SHAPES.items():
    print(f"{event:16} -> {shape}")
print(f"\nshapes: {len(SHAPES)}, reasoning hidden, proof visible")
