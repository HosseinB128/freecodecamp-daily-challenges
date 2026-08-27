"""
Challenge: Matrix Builder
Source: freeCodeCamp
Date: 2025-11-05
Problem: Given two integers (a number of rows and a number of columns), return
a matrix (an array of arrays) filled with zeros (0) of the given size.
For example, given 2 and 3, return:
[
  [0, 0, 0],
  [0, 0, 0]
]
"""


def build_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


# Tests
assert build_matrix(2, 3) == [[0, 0, 0], [0, 0, 0]]
assert build_matrix(3, 2) == [[0, 0], [0, 0], [0, 0]]
assert build_matrix(4, 3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert build_matrix(9, 1) == [[0], [0], [0], [0], [0], [0], [0], [0], [0]]

print("All tests passed!")

