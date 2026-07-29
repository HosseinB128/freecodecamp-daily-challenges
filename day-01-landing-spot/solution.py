"""
Challenge: Landing Spot
Source: freeCodeCamp - Space Week Day 4
Date: 2025-10-07

Given a matrix of numbers (list of lists) representing potential landing
spots for a rover, find the safest landing spot.

Rules:
- Each cell contains a number from 0-9.
- A 0 represents a potential landing spot.
- Any non-zero number is dangerous to land on; higher numbers mean more danger.
- The safest spot is the 0 cell whose surrounding neighbors (up, down, left,
  right - diagonals are ignored) have the lowest total danger.
- Out-of-bounds neighbors (for edges and corners) are ignored.
- Return the indices [row, col] of the safest landing spot. There will
  always be exactly one safest spot.

Example:
    [[1, 0],
     [2, 0]]
    -> [0, 1]
"""


def find_landing_spot(matrix):
    row = len(matrix)
    col = len(matrix[0])
    least_dangerous_spot = None
    safest_spot = None

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                danger_level = 0
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for ni, nj in neighbors:
                    if 0 <= ni < row and 0 <= nj < col:
                        danger_level += matrix[ni][nj]

                if least_dangerous_spot is None or danger_level < least_dangerous_spot:
                    least_dangerous_spot = danger_level
                    safest_spot = [i, j]

    return safest_spot


# Tests
assert find_landing_spot([[1, 0], [2, 0]]) == [0, 1]
assert find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) == [1, 1]
assert find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) == [2, 2]
assert find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) == [2, 1]
print("All tests passed!")

