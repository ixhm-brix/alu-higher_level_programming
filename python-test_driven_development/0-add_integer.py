#!/usr/bin/python3
"""This module provides a function to add two integers or floats.
It validates inputs and casts floats to integers before addition.
The module raises TypeError for non-integer/float inputs.
This is part of the python-test_driven_development project.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.

    Args: a (int or float), b (int or float, default 98)
    Returns: int - the sum of a and b cast to integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
