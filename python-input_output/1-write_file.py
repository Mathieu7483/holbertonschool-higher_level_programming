#!/usr/bin/python3
"""Module that define a write"""


def write_file(filename="", text=""):
    """function that write a file"""

    with open(filename, mode='w', encoding="utf-8") as f:
        num_written = f.write(text)
        return num_written
