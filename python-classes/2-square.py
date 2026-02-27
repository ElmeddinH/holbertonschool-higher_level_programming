#!/usr/bin/python3
"""Module that defines a Square class with size validation"""


class Square:
    """Class that defines a square with validated size attribute"""
    def __init__(self, size=0):
        """Initialize a square with a given size
        
        Args:
            size: size of the square (default 0)
            
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
