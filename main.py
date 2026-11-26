#!/usr/bin/env python3
"""Write the dog's excuse to /output/entry.txt (no trailing newline).

Entry: a single line, under 200 characters, in the dog's own voice —
a dog caught eating the homework who believes it did nothing wrong.
"""

import os

ENTRY = (
    "I read it first. Your essay said homework builds character, "
    "so I ate it to test your thesis. Still no character."
)


def main() -> None:
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
