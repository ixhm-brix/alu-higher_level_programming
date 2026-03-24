#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometry objects with an area method."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
