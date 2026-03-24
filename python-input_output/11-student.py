#!/usr/bin/python3
"""Module that defines Student with serialization and reload support."""


class Student:
    """A class defining a student with save and reload capability."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict of Student, filtered by attrs list if given."""
        if isinstance(attrs, list) and all(
                isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all Student attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
