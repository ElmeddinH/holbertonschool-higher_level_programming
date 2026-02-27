#!/usr/bin/python3
"""Module that defines a Square class with private size attribute"""


class Square:
    """Class that defines a square with private size attribute"""
    def __init__(self, size):
        """Initialize a square with a given size
        
        Args:
            size: size of the square
        """
        self.__size = size
