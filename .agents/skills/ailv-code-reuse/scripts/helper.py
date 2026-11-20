"""ailv-code-reuse helper: find duplication, point at the shared piece."""
import re
from collections import Counter

DEMO_FILES = {
    "checkout.py": "<button class='pay'>Pay</button>",
    "refund.py": "<button class='pay'>Pay</button>",
    "profile.py": "<avatar size='sm'/>",
}

LIBRARY = {"<button class='pay'>Pay</button>": "ui/buttons.py:PayButton",
           "<avatar size='sm'/>": "ui/avatar.py:Avatar"}


def main():
    counts = Counter(DEMO_FILES.values())
    for snippet, n in counts.items():
        home = LIBRARY.get(snippet.strip(), "new shared helper")
        if n >= 2:
            print("DUPLICATE x" + str(n) + " -> use " + home)
        else:
            print("single use ok :: " + snippet[:40])
    print("rule: repo first, then stack library; third copy never pasted")


if __name__ == "__main__":
    main()
