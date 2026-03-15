#!/usr/bin/python3
"""Module that defines class_to_json function"""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object

    Args:
        obj: instance of a Class

    Returns:
        Dictionary description with simple data structure for JSON
    """
    return obj.__dict__
