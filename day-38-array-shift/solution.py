"""
Challenge: Array Shift
Source: freeCodeCamp
Date: 2025-11-13
Problem: Given an array and an integer representing how many positions to
shift the array, return the shifted array. A positive integer shifts the
array to the left. A negative integer shifts the array to the right. The
shift wraps around the array.
Example: shift_array([1, 2, 3], 1) returns [2, 3, 1]
"""


def shift_array(arr, n):
    n %= len(arr)
    return arr[n:] + arr[:n]


# Tests
assert shift_array([1, 2, 3], 1) == [2, 3, 1]
assert shift_array([1, 2, 3], -1) == [3, 1, 2]
assert shift_array(["alpha", "bravo", "charlie"], 5) == ["charlie", "alpha", "bravo"]
assert shift_array(["alpha", "bravo", "charlie"], -11) == ["bravo", "charlie", "alpha"]
assert shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) == [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
print("All tests passed!")

