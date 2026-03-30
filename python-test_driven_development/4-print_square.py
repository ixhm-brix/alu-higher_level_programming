#!/usr/bin/python3
"""This module provides a function to print a square using # characters.
Size must be a non-negative integer.
Raises TypeError or ValueError for invalid inputs.
This is part of the python-test_driven_development project.
"""


def print_square(size):
    """Print a square of # characters with side length size.

    Args: size (int) - the length of each side of the square
    Returns: None
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
