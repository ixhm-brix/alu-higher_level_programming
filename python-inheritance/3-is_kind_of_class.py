#!/usr/bin/python3
"""Module that provides a function to check class or subclass instance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it."""
    return isinstance(obj, a_class)
