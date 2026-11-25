"""The Excuse That Almost Works — make.fun entry.

Writes the single line a gamer texts the boss to skip work during
GTA 6 launch week: a smart lock that updated overnight and locked
him inside his own flat. Specific, boring, almost believable — and
the joke is the software update doing the betraying.
"""

import os

LINE = "Sorry, my smart lock updated overnight and locked me inside my flat, locksmith can't come until this afternoon."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Competition caps: 1-140 characters, at most 20 words, one line.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert len(LINE.split()) <= 20, "line must be at most 20 words"
    assert "\n" not in LINE and LINE.strip() == LINE, "line must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
