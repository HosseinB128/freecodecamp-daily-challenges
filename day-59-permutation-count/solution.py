"""
Challenge: Permutation Count
Source: freeCodeCamp
Date: 2025-12-04
Problem: Given a string, return the number of distinct permutations that can be
formed from its characters. Repeated characters must not produce duplicate
arrangements, and the string contains only letters (A-Z, a-z).
Example: "abb" -> 3 (abb, bab, bba)
"""

import collections
import math

def count_permutations(text):
    letter_counts = collections.Counter(text)
    numerator = math.factorial(len(text))
    denominator = 1
    for count in letter_counts.values():
        denominator *= math.factorial(count)

    return numerator // denominator


# Tests
assert count_permutations("abb") == 3
assert count_permutations("abc") == 6
assert count_permutations("racecar") == 630
assert count_permutations("freecodecamp") == 39916800
print("All tests passed!")

