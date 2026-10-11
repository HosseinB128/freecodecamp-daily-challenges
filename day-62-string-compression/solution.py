"""
Challenge: String Compression
Source: freeCodeCamp
Date: 2025-12-07
Problem: Given a string sentence, return a compressed version of the sentence
where consecutive duplicate words are replaced by the word followed by the
number of times it repeats in parentheses. Only consecutive duplicates are
compressed, and words are separated by single spaces.
Example: "yes yes yes please" → "yes(3) please"
"""

from itertools import groupby


def compress_string(sentence):
    parts = []
    for word, group in groupby(sentence.split()):
        count = len(list(group))
        parts.append(f"{word}({count})" if count > 1 else word)
    return " ".join(parts)


# Tests
assert compress_string("yes yes yes please") == "yes(3) please"
assert compress_string("I have have have apples") == "I have(3) apples"
assert compress_string("one one three and to the the the the") == "one(2) three and to the(4)"
assert compress_string("route route route route route route tee tee tee tee tee tee") == "route(6) tee(6)"
print("All tests passed!")

