#!/usr/bin/python3
"""This module provides a function to print text with indentation.
It adds 2 newlines after each occurrence of . ? or : characters.
Leading and trailing spaces are stripped from each line.
This is part of the python-test_driven_development project.
"""


def text_indentation(text):
    """Print text with 2 newlines after each '.', '?' or ':' character.

    Args: text (str) - the text to format and print
    Returns: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
