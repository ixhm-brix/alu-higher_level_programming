#!/usr/bin/python3
"""This module provides a function to divide all elements of a matrix.
It validates the matrix structure, element types, and divisor.
Returns a new matrix rounded to 2 decimal places.
This is part of the python-test_driven_development project.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimal places.

    Args: matrix (list of lists of int/float), div (int or float)
    Returns: new matrix with each element divided by div
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(err_matrix)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(err_matrix)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(err_matrix)
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
