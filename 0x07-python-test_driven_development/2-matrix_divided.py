#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divide(matrix, div):
    """Divides all elements of the matrix by div.
    Args:
        matrix: list of lists containing int or float.
        div: number to divide by.
    Returns:
        list: list of lists representing divided matrix.
    Raises:
        TypeError: If matrix is not list of lists.
        TypeError: If sublists are not all same.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for xx in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")