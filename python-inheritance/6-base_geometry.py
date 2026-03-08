#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area method"""

    def area(self):
        """Raise an exception for area method

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
