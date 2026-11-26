"""Entry program for the make.fun bounty "The Funniest Excuse for
Skipping a Meeting".

When run, it writes the entry's one excuse line to /output/entry.txt,
which is where the competition's gate scorer looks for it. The line is
a single excuse for skipping a pointless work meeting, kept well under
the competition's 200-character cap.

Only the Python 3 standard library is used.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

EXCUSE = (
    "Sorry, I can't make the meeting — my calendar and I are in couples "
    "therapy, and it says I keep overcommitting."
)


def write_entry(path: Path, text: str) -> None:
    """Write the entry text to *path* as UTF-8, creating /output if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    write_entry(OUTPUT_PATH, EXCUSE)


if __name__ == "__main__":
    main()
