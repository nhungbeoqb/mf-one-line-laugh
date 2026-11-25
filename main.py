#!/usr/bin/env python3
"""One Line, One Laugh — the self-checkout plays judge and jury.

Writes one funny line (1-140 chars) to /output/entry.txt.
Pure Python 3 stdlib; deterministic.
"""

import os

LINE = (
    "The self-checkout accused me of stealing my own groceries, "
    "so I apologised to the machine and it let me off with a warning."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
