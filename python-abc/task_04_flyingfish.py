#!/usr/bin/env python3
"""
Module that explores multiple inheritance and MRO with 
Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """Class representing a Fish"""

    def swim(self):
        """Prints the swimming action of a fish"""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish"""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird"""

    def fly(self):
        """Prints the flying action of a bird"""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish, 
    inherits from both Fish and Bird.
    """

    def fly(self):
        """Prints the flying action of a flying fish"""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints the swimming action of a flying fish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the habitat of a flying fish"""
        print("The flying fish lives both in water and the sky!")
