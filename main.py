#!/usr/bin/env python3
"""Write the entry sentence for 'One Sentence for a Traveler from 1800'.

The program writes exactly one sentence (at most 200 characters) to
/output/entry.txt. The sentence explains the modern internet to a time
traveler from 1800 using only words and images a person of that year
could already know: roads, letters, books, songs, doors, horses.
"""

import os

SENTENCE = (
    "Picture every road on earth joined into one great road, so any "
    "letter, book, or song may reach any door in the blink of an eye, "
    "at any hour, with no horse at all."
)


# Words a traveler from 1800 could not know; the sentence must use none.
MODERN_WORDS = (
    "internet", "computer", "screen", "website", "email", "digital",
    "online", "wifi", "phone", "video", "data", "software", "network",
)


def main() -> None:
    text = SENTENCE.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} characters, over the 200 limit"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    words = {w.strip(".,;:!?").lower() for w in text.split()}
    bad = sorted(words & set(MODERN_WORDS))
    assert not bad, f"sentence uses words coined after 1800: {bad}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
