#!/usr/bin/python3
"""this a divided matrix module"""


def matrix_divided(matrix, div):
    """this function divide a matrix by an integer"""

    for row in matrix:
        for nb in row:
            if not isinstance(nb, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix \
must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]