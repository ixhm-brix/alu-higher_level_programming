#!/usr/bin/python3
"""Module that provides a function to look up object attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
