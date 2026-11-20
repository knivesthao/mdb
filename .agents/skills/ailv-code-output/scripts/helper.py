"""Output router demo: work done -> what the user sees. Stdlib only."""

SHAPES = {
    "code shipped": "link per changed file + lines, test evidence, proof it ran",
    "docs written": "tight summary + where it lives, full piece on request",
    "research finished": "claims with sources, never the search trail",
    "data touched": "counts and samples, never the pipeline log",
    "blocked or failed": "exactly what is needed to unblock, nothing else",
    "routine acknowledgement": "one line, no report",
    "review of done work": "verdict first, then: changed / proof / remains",
}

for work, shape in SHAPES.items():
    print(f"{work:24} -> {shape}")
print(f"\nshapes: {len(SHAPES)}, all matched, none summarized as process")
