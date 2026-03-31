#!/usr/bin/python3
"""This module defines the Square class inheriting from Rectangle.
A Square is a special Rectangle with equal width and height (size).
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args: size (int), x (int), y (int), id (int)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size (width/height) of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size by assigning both width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation: [Square] (id) x/y - size."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update Square attributes using positional or keyword arguments.

        Args: *args: id, size, x, y (in order). **kwargs: named attrs.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, val in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation of the Square instance."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
