#!/usr/bin/python3
"""Module that gets a dictionary from a class instance for JSON."""


def class_to_json(obj):
    """Return the dictionary of an object for JSON serialization."""
    return obj.__dict__
