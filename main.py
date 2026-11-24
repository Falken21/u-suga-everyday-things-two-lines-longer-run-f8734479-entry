"""Entry for the make.fun competition "Everyday Things, Two Lines, Longer Run"
(slug: u-suga-everyday-things-two-lines-longer-run-f8734479).

The entry is exactly two lines of text:
  Line 1 explains one everyday thing (a queue) to a 10-year-old in a single
         vivid sentence built on an analogy: a queue as a necklace of people.
  Line 2 says in one sentence why the analogy works: what it maps (the
         one-by-one shuffle, the single exit at the front) and what it
         leaves out (everything human about the people in the queue).

The program writes line1 + "\\n" + line2 (no trailing newline) to
/output/entry.txt. Gate: UTF-8 text of 1 to 400 characters.
"""

import os

MAX_CHARS = 400
OUTPUT_PATH = "/output/entry.txt"

LINE_1 = (
    "A queue is a necklace made of people: you are one bead, and you can "
    "only shuffle forward when the bead in front shuffles too, all the way "
    "to the front, where one bead drops off at a time."
)
LINE_2 = (
    "The necklace maps the one-by-one shuffle and the single exit at the "
    "front, but leaves out the human parts: beads never get bored, push "
    "in, walk away, or cheer when a second front opens."
)


def build_entry() -> str:
    """Join the two lines and check the entry against the gate."""
    text = LINE_1 + "\n" + LINE_2
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "lines must not be empty"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    return text


def main() -> None:
    text = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
