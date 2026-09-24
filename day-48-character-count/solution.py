"""
Challenge: Character Count
Source: freeCodeCamp
Date: 2025-11-23
Problem: Given a sentence string, return an array with the count of each
character in alphabetical order. Upper and lowercase letters are treated as
the same letter. Numbers, spaces, punctuation, etc. are ignored. Each item is
formatted as "letter count" with a lowercase letter, and letters that do not
appear in the string are not returned.
Example: "hello world" → ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]
"""

from collections import Counter

def count_characters(sentence):
    counts = Counter(ch for ch in sentence.lower() if ch.isalpha())
    return [f"{ch} {n}" for ch, n in sorted(counts.items())]


# Tests
assert count_characters("hello world") == ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]
assert count_characters("I love coding challenges!") == [
    "a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1",
]
assert count_characters("// TODO: Complete this challenge ASAP!") == [
    "a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3",
]
assert count_characters("AaA") == ["a 3"]
assert count_characters("Zebra") == ["a 1", "b 1", "e 1", "r 1", "z 1"]
assert count_characters("12345 !!! ???") == []
assert count_characters("") == []
print("All tests passed!")

