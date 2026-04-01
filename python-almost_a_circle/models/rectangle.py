#!/usr/bin/python3
"""This module defines the Rectangle class inheriting from Base.
It includes validation for all attributes and area/display methods.
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base with width, height, x, y."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args: width (int), height (int), x (int), y (int), id (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with integer and positive value validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with integer and positive value validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x position of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x with integer and non-negative value validation."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y position of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y with integer and non-negative value validation."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle with # characters accounting for x and y."""
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return string: [Rectangle] (id) x/y - width/height."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update Rectangle attributes using positional or keyword arguments.

        Args: *args: id, width, height, x, y (in order). **kwargs: named attrs.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, val in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation of the Rectangle instance."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
