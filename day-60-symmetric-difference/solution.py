"""
Challenge: Symmetric Difference
Source: freeCodeCamp
Date: 2025-12-05
Problem: Given two arrays, return a new array containing the symmetric
difference of them. The symmetric difference between two sets is the set of
values that appear in either set, but not both. Return the values in the
order they first appear in the input arrays.
Example: difference([1, 2, 3], [3, 4, 5]) → [1, 2, 4, 5]
"""

from collections import Counter

def difference(arr1, arr2):
    return [key for key, value in Counter(arr1 + arr2).items() if value == 1]


# Tests
assert difference([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
assert difference(["a", "b"], ["c", "b"]) == ["a", "c"]
assert difference([1, "a", 2], [2, "b", "a"]) == [1, "b"]
assert difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]
print("All tests passed!")

