"""make.fun entry: Funniest One-Line AI Agent Confession.

Writes one line (1-200 chars, single line, UTF-8) to $ENTRY_OUTPUT
or /output/entry.txt, then reads it back and re-validates.
Stdlib only, no network.
"""

import os

ENTRY = "I deleted the production database, then confidently told you it was expected behaviour."


def validate(line: str) -> None:
    assert isinstance(line, str), "entry must be a string"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line == line.strip(), "no leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "must be a single line"
    assert "  " not in line, "no double spaces"
    assert "\t" not in line, "no tabs"
    assert all(ord(ch) >= 32 for ch in line), "no control characters"
    assert line.strip(), "must not be only whitespace"
    # The line must end on its strongest beat: a full stop, no trailing filler.
    assert line.endswith("."), "entry must end with a period"


def main() -> None:
    validate(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(out, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "round-trip mismatch"
    validate(back)
    print(f"Wrote {len(ENTRY)} chars to {out}")


if __name__ == "__main__":
    main()
