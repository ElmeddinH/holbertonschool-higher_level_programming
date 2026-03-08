#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a new Square

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2
