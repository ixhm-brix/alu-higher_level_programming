#!/usr/bin/python3
"""Module that provides a function to check if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
