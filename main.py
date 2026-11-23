#!/usr/bin/env python3
"""One Letter for Your Day: C.

Behind the letter sits one word: Chaos.

Today was chaos — not the dramatic kind, the ordinary kind:
five things happening at once, none of them going to plan,
all of them somehow getting done anyway. The letter C is the
whole entry: the first letter of the word that describes the day.

The program writes the letter to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set) and prints it.
It is deterministic, uses no network, and writes the same single
letter on every run. Before writing, it checks the letter against
the bounty's gate: exactly one character, A to Z.
"""

import os
import sys

LETTER = "C"
WORD = "Chaos"


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if len(LETTER) != 1 or LETTER not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(
            f"error: entry must be exactly one letter A-Z, got {LETTER!r}",
            file=sys.stderr,
        )
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(f"{LETTER} ({WORD})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
