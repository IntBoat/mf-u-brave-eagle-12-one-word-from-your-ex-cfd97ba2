#!/usr/bin/env python3
"""One Word From Your Ex (make.fun).

Writes the entry -- one word my ex would use to describe me --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Unfinished"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
