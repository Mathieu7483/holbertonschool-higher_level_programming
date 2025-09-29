#!/usr/bin/python3
"""Module that define a function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    new_content = ""

    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                new_content += line
                if search_string in line:
                    new_content += new_string
    except FileNotFoundError:
        return

    try:
        with open(filename, mode='w', encoding="utf-8") as f:
            f.write(new_content)
    except Exception as e:
        print(f"error not writing in file : {e}")
