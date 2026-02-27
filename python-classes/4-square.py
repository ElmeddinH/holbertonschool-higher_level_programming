#!/usr/bin/python3
"""Module that defines a Square class with getter and setter"""


class Square:
    """Class that defines a square with property getter and setter"""
    def __init__(self, size=0):
        """Initialize a square with a given size

        Args:
            size: size of the square (default 0)
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value: new size value

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2
