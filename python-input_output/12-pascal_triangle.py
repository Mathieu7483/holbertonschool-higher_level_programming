#!/usr/bin/python3
"""Module that define a pascal triangle function"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
     representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        prev_row = triangle[-1] if i > 0 else None

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)
    return triangle
