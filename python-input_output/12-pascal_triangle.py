#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row

    Args:
        n (int): num of rows in Pascal's triangle

    Returns:
        list: list of lists of ints representing triangle
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
