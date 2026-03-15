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

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance

        Returns:
            Dictionary representation of the student
        """
        return self.__dict__
