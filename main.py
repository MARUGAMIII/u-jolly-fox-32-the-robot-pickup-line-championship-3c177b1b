#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt (or the path in ENTRY_OUTPUT).

Standard library only. Fully deterministic: the same line every run.

Before writing, the line is checked against the competition gate
(RULES.txt): UTF-8 text of 1 to 200 characters, a single line, not
only white space. The program refuses to write an entry that would
fail the gate instead of letting the grader catch it.
"""

import os
import sys

LINE = (
    "I was programmed to find the perfect match. "
    "Then I met you and deleted the program."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Raise ValueError if the line would fail the competition gate."""
    if not line or line.isspace():
        raise ValueError("entry is empty or only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    line.encode("ascii")  # entry is plain ASCII: no em dash, no smart quotes


def main() -> int:
    try:
        validate(LINE)
    except (ValueError, UnicodeEncodeError) as error:
        print(f"entry fails the gate: {error}", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
