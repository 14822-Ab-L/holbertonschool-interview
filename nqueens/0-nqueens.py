#!/usr/bin/python3
"""Solve the N Queens problem using backtracking."""

import sys


def is_safe(board, row, col):
    """Check whether a queen can be placed safely."""

    for previous_row in range(row):
        previous_col = board[previous_row]

        # Check for another queen in the same column.
        if previous_col == col:
            return False

        # Check for another queen on the same diagonal.
        if abs(previous_row - row) == abs(previous_col - col):
            return False

    return True


def solve(board, row, n):
    """Find and print all possible N Queens solutions."""

    if row == n:
        solution = [[r, board[r]] for r in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(board, 0, n)
