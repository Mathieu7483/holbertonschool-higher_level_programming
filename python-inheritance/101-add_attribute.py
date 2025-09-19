#!/usr/bin/python3
"""Module that define a Myint class"""


class MyInt(int):
    """
    A class that inherits from 'int' and reverses
    the equality (==) and inequality (!=) operators.
    """

    def __eq__(self, other):

        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)


def add_attribute(obj, attr_name, value):
    """
   Adds a new attribute to an object if possible.

Args:
obj: The object to add the attribute to.
attr_name: The name of the attribute to add.
value: The value of the attribute.

Raises:
TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
