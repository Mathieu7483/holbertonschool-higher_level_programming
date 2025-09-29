#!/usr/bin/python3
"""Module that define an append to a text"""


def append_write(filename="", text=""):
    """function that append a text to a file"""

    with open(filename, mode='a', encoding="utf-8") as f:
        num_written = f.write(text)
        return num_written
