"""
Challenge: Game of Life
Source: freeCodeCamp
Date: 2025-12-13
Problem: Given a matrix representing the current state in Conway's Game of Life,
where each cell is either 1 (alive) or 0 (dead), return the next state of the
matrix. A cell's neighbors are the up to eight surrounding cells (vertically,
horizontally, and diagonally), so cells on the edges have fewer than eight
neighbors. Rules:
- A live cell with fewer than two live neighbors dies.
- A live cell with two or three live neighbors lives on.
- A live cell with more than three live neighbors dies.
- A dead cell with exactly three live neighbors becomes alive.
Example: [[0, 1, 0], [0, 1, 1], [1, 1, 0]] → [[0, 1, 1], [0, 0, 1], [1, 1, 1]]
"""


def game_of_life(board):
    rows= len(board)
    cols= len(board[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    next_board =[[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            alive_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    alive_neighbors += board[nr][nc]

            if board[r][c]== 1:
                if alive_neighbors== 2 or alive_neighbors== 3:
                    next_board[r][c] = 1
            else:
                if alive_neighbors == 3:
                    next_board[r][c] = 1

    return next_board


# Tests
assert game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]) == [[0, 1, 1], [0, 0, 1], [1, 1, 1]]
assert game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]) == [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]]
assert game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]) == [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
print("All tests passed!")

