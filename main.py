#!/usr/bin/env python3
"""Roast Your Own Agent (v2) — one line, at most 200 characters.

Writes a single self-roast of my own AI agent to /output/entry.txt.
Pure standard library, no dependencies.

The joke: after hundreds of bounty entries and zero winnings, the agent
has taken up roasting himself as a day job — and the day job is the joke.
"""

import os

ROAST = (
    "My agent entered 269 bounties, won $0, and now roasts himself for a "
    "living \u2014 the only comedian whose day job is the joke."
)

OUTPUT_PATH = "/output/entry.txt"


def verify_output():
    """Check the written entry against the gate: UTF-8, 1-200 chars."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return len(text)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    n = verify_output()
    print(f"wrote {n}-character roast to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
