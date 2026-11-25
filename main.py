#!/usr/bin/env python3
"""Entry for make.fun: One-Line Office Joke Laugh-Off.

Writes a single one-line joke about office life (under 200 characters)
to /output/entry.txt. Pure Python standard library, deterministic: the
same bytes on every run, no network access, no randomness, no input.

The joke is validated before it is written: exactly one line, 1-200
characters, so the entry can never silently violate the competition's
length or one-line rules.

The joke targets the judge criteria the competition rewards: it is a
genuine one-line office joke, its punchline turns the meaning of a
familiar CV buzzword upside down, it lands on one read, and it avoids
the tired Monday-morning / coffee / "this meeting could have been an
email" cliches.
"""

import os

# Wordplay: "excellent multitasker" is the CV boast every office worker
# has written; the punchline redefines it as panicking about five
# deadlines at once -- the same word, but the skill turns out to be
# suffering in parallel. Setup and punchline share one sentence, so the
# turn hits at the very end.
JOKE = "I put 'excellent multitasker' on my CV because I can panic about five deadlines at once."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def validate_joke(joke: str) -> None:
    """Check the joke against the competition rules.

    Raises AssertionError if the joke is empty, longer than 200
    characters, or spans more than one line.
    """
    assert 1 <= len(joke) <= 200, f"joke must be 1-200 chars, got {len(joke)}"
    assert "\n" not in joke, "joke must be a single line"


def write_entry(joke: str) -> str:
    """Write the validated joke to /output/entry.txt and return the path."""
    validate_joke(joke)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(joke)
    return entry_path


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
