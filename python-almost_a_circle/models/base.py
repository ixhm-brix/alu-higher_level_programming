#!/usr/bin/python3
"""This module defines the Base class for the almost_a_circle project.
It manages id attributes and provides JSON serialization utilities.
"""
import json
import os


class Base:
    """Base class to manage id attribute for all future classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance with optional id.

        Args: id (int): The id to assign. Auto-increments if None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args: list_dictionaries (list): List of dictionaries to serialize.
        Returns: str - JSON string, or "[]" if None/empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args: list_objs (list): List of Base instances to save.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string.

        Args: json_string (str): JSON string of a list of dictionaries.
        Returns: list - the deserialized list, or [] if None/empty.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args: **dictionary: Key/value pairs of attributes to assign.
        Returns: An instance of cls with all attributes set.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            dummy = Rectangle(1, 1)
        else:
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file.

        Returns: list of instances of cls, or [] if file does not exist.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_string = f.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
