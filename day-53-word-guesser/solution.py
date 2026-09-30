"""
Challenge: Word Guesser
Source: freeCodeCamp
Date: 2025-11-28
Problem: Given a secret word and a guess of the same length, return a string
of digits: "2" if the letter is correct and in the right position, "1" if the
letter is in the secret word but in the wrong position, "0" if it is not in
the secret word. Each letter of the secret word can be used at most once.
Exact matches are assigned first, then partial matches left to right.
Example: compare("APPLE", "POPPA") → "10201"
"""

from collections import Counter

def compare(secret, guess):
    result = ["0"] * len(guess)
    remaining = Counter()

    for i, (s, g) in enumerate(zip(secret, guess)):
        if s == g:
            result[i] = "2"
        else:
            remaining[s] += 1

    for i, g in enumerate(guess):
        if result[i] == "0" and remaining[g] > 0:
            result[i] = "1"
            remaining[g] -= 1

    return "".join(result)


# Tests
assert compare("APPLE", "POPPA") == "10201"
assert compare("REACT", "TRACE") == "11221"
assert compare("DEBUGS", "PYTHON") == "000000"
assert compare("JAVASCRIPT", "TYPESCRIPT") == "0000222222"
assert compare("ORANGE", "ROUNDS") == "110200"
assert compare("WIRELESS", "ETHERNET") == "10021000"
print("All tests passed!")

