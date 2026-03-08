#!/usr/bin/python3
"""Module that defines is_same_class function"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of the specified class

    Args:
        obj: the object to check
        a_class: the class to compare with

    Returns:
        True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
