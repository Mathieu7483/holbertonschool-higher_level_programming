#!/usr/bin/python3
"""
Module that define a print of a square with # character
"""


def print_square(size):
    """
    function that prints a square with size # character
    size is a integer > 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
