#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited from a_class

    Args:
        obj: the object to check
        a_class: the class to compare with

    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
