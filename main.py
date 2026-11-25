#!/usr/bin/env python3
"""Aica Office Laugh — make.fun entry for
u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

Writes one single-line joke about office life to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace, on a single line.
"""

import os
import sys

# The joke: one line, well under 200 characters.
# True to office life (the Wi-Fi going down), surprising turn
# (eye contact as a novelty), tight, and read aloud in one breath.
JOKE = (
    "The Wi-Fi went down for ten minutes, and for the first time "
    "ever, everyone in the office actually made eye contact."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    """Validate the joke and write it, byte-identical every run."""
    text = validate(JOKE)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # No trailing newline: the file holds exactly the joke's bytes.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
