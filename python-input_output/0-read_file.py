#!/usr/bin/python3
"""Module that define a read"""


def read_file(filename=""):
    """function that read a file"""

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
