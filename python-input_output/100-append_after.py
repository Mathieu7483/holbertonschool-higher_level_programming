#!/usr/bin/python3
"""Module that define a function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    new_content = ""

    with open(filename, encoding="utf-8") as f:
         for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string


    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(new_content)
