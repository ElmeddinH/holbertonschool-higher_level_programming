#!/usr/bin/env python3
"""
Module that defines the CountedIterator class to keep track of iterations.
"""


class CountedIterator:
    """
    Custom iterator that wraps an iterable and keeps track of how many 
    items have been iterated over.
    """

    def __init__(self, iterable):
        """Initialize the iterator and the counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the current count of fetched items"""
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
