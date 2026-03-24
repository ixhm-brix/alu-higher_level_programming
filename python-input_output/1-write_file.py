#!/usr/bin/python3
"""Module that provides a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
