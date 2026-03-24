#!/usr/bin/python3
"""Module that provides a function to convert an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)
