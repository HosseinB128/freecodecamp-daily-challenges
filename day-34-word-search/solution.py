"""
Challenge: Word Search
Source: freeCodeCamp
Date: 2025-11-09

Given a matrix (an array of arrays) of single letters and a word to find,
return the start and end indices of the word in the matrix.

- The given matrix will be filled with all lowercase letters (a-z).
- The word to find will always be in the matrix exactly once.
- The word to find will always be in a straight line in one of these directions:
  left to right, right to left, top to bottom, or bottom to top.
"""


def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    word_len = len(word)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != word[0]:
                continue
            for di, dj in directions:
                end_i = i + di * (word_len - 1)
                end_j = j + dj * (word_len - 1)
                # check end point is inside the matrix
                if not (0 <= end_i < rows and 0 <= end_j < cols):
                    continue
                # check every letter along the path
                match = True
                for k in range(word_len):
                    r = i + di * k
                    c = j + dj * k
                    if matrix[r][c] != word[k]:
                        match = False
                        break
                if match:
                    return [[i, j], [end_i, end_j]]
    return None


# Tests
assert find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat") == [[0, 1], [2, 1]]
assert find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog") == [[0, 0], [0, 2]]
assert find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish") == [[3, 3], [0, 3]]
assert find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox") == [[1, 3], [1, 1]]

print("All tests passed!")

