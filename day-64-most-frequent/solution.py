"""
Challenge: Most Frequent
Source: freeCodeCamp
Date: 2025-12-09
Problem: Given an array of elements, return the element that appears most
frequently. There will always be a single most frequent element.
Example: most_frequent(["a", "b", "a", "c"]) -> "a"
"""

import collections

def most_frequent(arr):
    return collections.Counter(arr).most_common()[0][0]


# Tests
assert most_frequent(["a", "b", "a", "c"]) == "a"
assert most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) == 2
assert most_frequent([True, False, "False", "True", False]) is False
assert most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) == 40
print("All tests passed!")

