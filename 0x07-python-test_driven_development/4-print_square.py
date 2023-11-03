#!/usr/bin/python3


def print_square(size):
    """Method for printing a suqre.
    Args:
        size: the int size of the square

    Rqises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    print((("#" * size + "\n") * size), end="")


if __name__ = "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
