#!/usr/bin/env python3
"""
Module that demonstrates the use of Mixins.
Contains SwimMixin, FlyMixin, and Dragon classes.
"""


class SwimMixin:
    """Mixin class that provides swimming functionality"""

    def swim(self):
        """Prints the swimming action"""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying functionality"""

    def fly(self):
        """Prints the flying action"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a Dragon.
    Inherits swimming and flying abilities from mixins.
    """

    def roar(self):
        """Prints the roaring action of a dragon"""
        print("The dragon roars!")
