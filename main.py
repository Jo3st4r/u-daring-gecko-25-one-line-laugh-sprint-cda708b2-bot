#!/usr/bin/env python3
"""One-Line Laugh Sprint — u-daring-gecko-25-one-line-laugh-sprint-cda708b2.

Writes a single original funny line (<=200 characters, everyday life) to
/output/entry.txt. Stdlib only; no network, no randomness, no I/O besides
the one output file.

The joke is built from three named beats so each turn of the gag is visible
in the code:

* SETUP — the plan: 5 alarms to wake up at 6.
* SNOOZE — the failure: every single one snoozed.
* BLAME — the twist: the clock gets blamed, not the sleeper.

Five alarms set, five alarms snoozed, and the alarm clock still takes
the blame for being unreliable.
"""

import os

# The three beats of the joke, joined in entry_text().
SETUP = "I set 5 alarms to wake up at 6"
SNOOZE = "snoozed all 5"
BLAME = "and still blamed the alarm clock for being unreliable."

# The competition caps the entry at 200 characters; the line is 101.
MAX_CHARS = 200

ENTRY = "I set 5 alarms to wake up at 6, snoozed all 5, and still blamed the alarm clock for being unreliable."


def entry_text() -> str:
    """Join the three beats into the one-line joke."""
    return f"{SETUP}, {SNOOZE}, {BLAME}"


def main() -> None:
    text = entry_text()
    # Guard the three things the gate checks: the line itself, that it
    # fits the 200-character limit with room to spare, and that it is
    # exactly one line with no stray newline at the end.
    assert text == ENTRY, "joined line drifted from the entry sentence"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
