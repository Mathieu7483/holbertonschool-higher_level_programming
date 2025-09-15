#!/usr/bin/python3
"""Module who define a square class."""


class Square:
    """Class who define an square with size argument."""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.area
