#!/usr/bin/python3
"""Module that defines Student class"""


class Student:
    """Student class with first_name, last_name, and age attributes"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance

        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        Args:
            attrs: list of attribute names to retrieve (optional)

        Returns:
            Dictionary representation of the student
        """
        if attrs is None:
            return self.__dict__
        
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
