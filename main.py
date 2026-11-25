"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of gravity to /output/entry.txt
and to entry.txt next to this script.
"""

import os

ENTRY = "One star. Gravity drops everything I own at least once and has never once caught a single thing."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"entry ({len(ENTRY)} chars): {ENTRY}")


if __name__ == "__main__":
    main()
