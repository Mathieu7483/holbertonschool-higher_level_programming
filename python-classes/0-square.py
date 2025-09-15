#!/usr/bin/python3
"""Write an empty class Square that defines a square"""


class square:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def is_square(self):
        return self.width == self.height
