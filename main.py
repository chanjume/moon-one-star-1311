#!/usr/bin/env python3
"""Write a one-star review of the Moon to /output/entry.txt.

The line (110 characters, inside the 120 gate): the Moon is reviewed like
a bad product -- it moved the reviewer's tide, flooded Dave's kayak at
3:04 a.m., then hid behind a cloud. Two specific details (the 3:04 a.m.
flood, the cloud) plus a named victim (Dave) and a real-review closer
("No apology, no refund"), with a second twist: after causing the flood
it ducks behind a cloud instead of owning it. The grievance is Moon-only -- only the Moon
moves tides -- not the obvious craters/cheese/brightness jokes.
"""
import os

TEXT = (
    "1 star. Moon moved my tide, flooded Dave's kayak at 3:04 a.m., "
    "then hid behind a cloud. No apology, no refund."
)


def main():
    assert 1 <= len(TEXT) <= 120, f"text must be 1-120 characters, got {len(TEXT)}"
    assert TEXT.strip() == TEXT, "no leading/trailing whitespace"
    assert "\n" not in TEXT, "exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
