#!/usr/bin/env python3
"""
Module that defines a Shape abstract class, Circle and Rectangle subclasses,
and a shape_info function to demonstrate duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a shape"""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter"""
        pass


class Circle(Shape):
    """Class representing a Circle, inherits from Shape"""

    def __init__(self, radius=0):
        """Initialize a Circle with a radius"""
        self.radius = abs(radius)

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a Rectangle, inherits from Shape"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
