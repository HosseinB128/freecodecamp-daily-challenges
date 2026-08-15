"""
Challenge: Hidden Treasure
Source: freeCodeCamp
Date: 2025-10-24
Problem: Given a 2D array representing a map of the ocean floor that includes
a hidden treasure, and an array with the coordinates ([row, column]) for the
next dive of your treasure search, return "Empty", "Found", or "Recovered"
using the following rules:
- The given 2D array will contain exactly one unrecovered treasure, which
  will occupy multiple cells.
- Each cell in the 2D array will contain one of the following values:
    "-": No treasure.
    "O": A part of the treasure that has not been found.
    "X": A part of the treasure that has already been found.
- If the dive location has no treasure, return "Empty".
- If the dive location finds treasure, but at least one other part of the
  treasure remains unfound, return "Found".
- If the dive location finds the last unfound part of the treasure, return
  "Recovered".
Example: dive([["-", "X"], ["-", "X"], ["-", "O"]], [2, 1]) -> "Recovered"
"""

def dive(map, coordinates):
    row, col = coordinates

    if map[row][col] == "-":
        return "Empty"

    map[row][col] = "X"
    remains = any("O" in r for r in map)
    return "Found" if remains else "Recovered"


# Tests
assert dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) == "Recovered"
assert dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) == "Empty"
assert dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) == "Found"
assert dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) == "Found"
assert dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) == "Recovered"
assert dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) == "Empty"

print("All tests passed!")

