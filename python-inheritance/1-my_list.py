#!/usr/bin/python3
"""Module who define a Mylist class."""


class MyList(list):
    """
    A class that inherits from list ans sorted it.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order,
        """
        print(sorted(self))
