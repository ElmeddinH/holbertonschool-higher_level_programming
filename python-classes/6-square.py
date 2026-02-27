#!/usr/bin/python3
"""Module that defines a Square class with position"""


class Square:
    """Class that defines a square with position"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position

        Args:
            size: size of the square (default 0)
            position: position of the square (default (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value: new position value

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters with position offset"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
