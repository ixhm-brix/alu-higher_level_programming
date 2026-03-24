#!/usr/bin/python3
"""Module that defines Square with a custom string description."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square class with its own string description."""

    def __init__(self, size):
        """Initialize Square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
