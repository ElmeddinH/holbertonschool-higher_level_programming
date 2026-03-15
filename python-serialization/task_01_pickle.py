#!/usr/bin/env python3
"""Module for pickling custom classes"""
import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes"""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance

        Args:
            name: name of the person (string)
            age: age of the person (integer)
            is_student: student status (boolean)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file

        Args:
            filename: name of the file to save to
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file

        Args:
            filename: name of the file to load from

        Returns:
            CustomObject instance or None if error
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
