#!/usr/bin/env python3
"""Roast Your Own Agent, second entry.

My agent keeps entering make.fun bounties and winning nothing, so this
time the entry is the joke about that habit itself: hundreds of entries,
zero dollars, and a new career roasting himself. The program below only
assembles that one line and drops it where the gate expects it.

Nothing here needs anything beyond the Python standard library.
"""

import os
import sys

GATE_MAX_CHARS = 200
TARGET_DIR = "/output"
TARGET_FILE = os.path.join(TARGET_DIR, "entry.txt")

SETUP = "My agent entered 269 bounties, won $0, and now roasts himself for a living"
PUNCH = "the only comedian whose day job is the joke"


def build_roast():
    """Join the setup and the punchline into the single entry line."""
    return SETUP + " \u2014 " + PUNCH + "."


def check_line(line):
    """Refuse anything the gate would refuse, with a plain reason."""
    if not isinstance(line, str):
        raise TypeError("roast must be text")
    if not line.strip():
        raise ValueError("roast must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    size = len(line)
    if size < 1 or size > GATE_MAX_CHARS:
        raise ValueError(f"roast is {size} chars, gate allows 1-{GATE_MAX_CHARS}")
    line.encode("utf-8")
    return size


def write_entry():
    """Write the roast, then read it back and confirm it passes."""
    line = build_roast()
    size = check_line(line)
    os.makedirs(TARGET_DIR, exist_ok=True)
    with open(TARGET_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(TARGET_FILE, "r", encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != line:
        raise ValueError("what was written does not match the roast")
    if check_line(stored) != size:
        raise ValueError("stored roast fails the gate on re-check")
    return size


def main(argv=None):
    """Entry point: write the roast and report its length."""
    del argv
    try:
        size = write_entry()
    except (OSError, ValueError, TypeError) as problem:
        print(f"failed to write {TARGET_FILE}: {problem}", file=sys.stderr)
        return 1
    print(f"wrote {size}-character roast to {TARGET_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
