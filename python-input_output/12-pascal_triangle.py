#!/usr/bin/python3
"""
function to generate Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    generate Pascal's triangle up to n rows.

    Args:
    n (int): number of rows in Pascal's triangle.

    Return: empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [last_row[j] + last_row[j+1] for j in
                range(len(last_row) - 1)]
        row.append(1)
        triangle.append(row)

    return triangle
