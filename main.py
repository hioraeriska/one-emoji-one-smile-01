#!/usr/bin/env python3
"""One Emoji, One Smile entry: writes exactly one emoji, nothing else.

The emoji is a hugging face: an open-armed hug aimed at a stranger,
warm at first glance, universal, and chosen rather than the default smiley.
"""

import os

EMOJI = "\U0001F917"

MIN_CHARS = 1
MAX_CHARS = 8


class EmojiValidator:
    """Runs every rule the bounty places on the single emoji."""

    def __init__(self, text):
        self.text = text

    def _require_content(self):
        if not self.text or self.text.strip() == "":
            raise ValueError("emoji must not be blank or only whitespace")

    def _require_length(self):
        size = len(self.text)
        if size < MIN_CHARS or size > MAX_CHARS:
            raise ValueError(
                "emoji must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, size)
            )

    def _require_single_emoji(self):
        if len(self.text) != 1:
            raise ValueError(
                "entry must be exactly one emoji, got %d characters" % len(self.text)
            )

    def validate(self):
        self._require_content()
        self._require_length()
        self._require_single_emoji()
        return self.text


def write_entry(emoji, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(emoji)
    return target


def main():
    emoji = EmojiValidator(EMOJI).validate()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(emoji, out_dir)


if __name__ == "__main__":
    main()
