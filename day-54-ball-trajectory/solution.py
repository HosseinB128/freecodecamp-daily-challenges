"""
Challenge: Ball Trajectory
Source: freeCodeCamp
Date: 2025-11-29
Problem: Given a matrix that includes the location of the ball (2) and the
previous location of the ball (1), return the matrix indices for the next
location of the ball. The ball moves in a straight line, and the edges of
the matrix are walls: hitting the top or bottom wall reverses the vertical
direction, hitting the left or right wall reverses the horizontal direction,
and hitting a corner reverses both.
Example: get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) → [2, 3]
"""


def get_next_location(matrix):
    rows = len(matrix)
    cols= len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                prev_r, prev_c = r, c
            elif matrix[r][c] == 2:
                cur_r, cur_c = r, c

    dr= cur_r - prev_r
    dc= cur_c - prev_c

    next_r = cur_r + dr
    next_c = cur_c + dc

    if next_r < 0 or next_r >= rows:
        dr = -dr
    if next_c < 0 or next_c >= cols:
        dc = -dc

    return [cur_r + dr, cur_c + dc]


# Tests
assert get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) == [2, 3]
assert get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) == [3, 0]
assert get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) == [1, 2]
assert get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) == [1, 1]
assert get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) == [2, 2]
print("All tests passed!")

