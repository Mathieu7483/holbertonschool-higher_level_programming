#!/usr/bin/python3
"""
Module that defines a base class for geometry-related classes.
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.
    """

    def area(self):
        """
        Raises:
        Exception: Always raised with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        "
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class to represent a square, inheriting from Rectangle."""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self._Square__size * self._Square__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
