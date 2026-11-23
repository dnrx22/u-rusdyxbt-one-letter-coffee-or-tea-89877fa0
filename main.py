"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to the output file and nothing else.
"A" means coffee, "B" means tea. This entry picks "A" (coffee):
a single letter, no word, no explanation, no punctuation, not even
a trailing newline — the letter is the whole entry.

Why coffee ("A")? The judge reads two letters at a time and picks
the one whose choice of coffee or tea feels more vivid, funnier or
truer. Coffee is the louder, bolder half of the pair — the morning
ritual, the strong start — so "A" is the letter this entry sends.
The program itself stays silent about that reasoning: the output
file holds the letter alone, exactly as the rules require.

The output directory comes from MAKEFUN_OUTPUT_DIR when set,
otherwise /output. The file is always named entry.txt.
"""

import os

LETTER = "A"  # A = coffee, B = tea
OUTPUT_FILENAME = "entry.txt"


def output_path() -> str:
    """Return the full path of the output file."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, OUTPUT_FILENAME)


def validate(letter: str) -> None:
    """Enforce the competition gate: exactly one character, "A" or "B".

    Rejects anything else — empty text, whitespace, punctuation,
    a newline, or more than one character — before anything is written.
    Also checks the UTF-8 encoding is exactly one byte, so no
    multi-byte lookalike can ever slip through as "one character".
    """
    if len(letter) != 1:
        raise ValueError(f"letter must be exactly 1 character, got {len(letter)}")
    if letter not in ("A", "B"):
        raise ValueError(f"letter must be 'A' or 'B', got {letter!r}")
    if letter.isspace():
        raise ValueError("letter must not be whitespace")
    if len(letter.encode("utf-8")) != 1:
        raise ValueError("letter must encode to exactly 1 byte")


def main() -> None:
    validate(LETTER)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = LETTER.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and re-validate what actually landed on disk.
    with open(path, "rb") as fh:
        written = fh.read()
    text = written.decode("utf-8")
    validate(text)
    print(f"Wrote {len(written)} byte(s) to {path}: {text!r} "
          f"({len(text)} character)")


if __name__ == "__main__":
    main()
