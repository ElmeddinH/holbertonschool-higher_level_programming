#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method for the animal's sound"""
        pass


class Dog(Animal):
    """Class representing a Dog, inherits from Animal"""

    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Class representing a Cat, inherits from Animal"""

    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
