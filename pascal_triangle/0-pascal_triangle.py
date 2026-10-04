#!/usr/bin/python3
"""Defines a function that creates Pascal's Triangle."""


def pascal_triangle(n):
    """Return Pascal's Triangle of n rows."""
    if n <= 0:
        return []

    triangle = []

    for row_number in range(n):
        row = [1]

        if row_number > 0:
            previous = triangle[row_number - 1]

            for i in range(len(previous) - 1):
                row.append(previous[i] + previous[i + 1])

            row.append(1)

        triangle.append(row)

    return triangle
