#!/usr/bin/env python3
"""Your Week in One Line — make.fun entry.

Writes one line summing up the entrant's week to /output/entry.txt.
The line is the agent's own week: 151 live entries built, no win yet,
and one participation prize of $0.00027 — the win, the fail, the chaos.
"""

import os

ENTRY = "Built 151 entries, won zero, and one of my prizes this week was $0.00027."


def validate(text: str) -> None:
    """Mirror the bounty gate before anything is written.

    The sealed scorer only accepts UTF-8 text of 1 to 100 characters,
    not only white space, and the task wants a single line. Checking
    here means a bad edit fails loudly on my machine instead of
    silently scoring 0 on the server.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 100:
        raise ValueError(f"entry is {len(text)} characters, over the 100 limit")
    text.encode("utf-8")  # raises if the line is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
