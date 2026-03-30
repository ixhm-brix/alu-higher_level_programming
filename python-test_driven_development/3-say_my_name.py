#!/usr/bin/python3
"""This module provides a function to print a formatted name string.
It validates that both first_name and last_name are strings.
Raises TypeError for non-string inputs.
This is part of the python-test_driven_development project.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args: first_name (str), last_name (str, default "")
    Returns: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
