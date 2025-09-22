#!/usr/bin/python3
"""
mudile that define an abstract method of a shape class"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi) * abs(self.radius**2)

    def perimeter(self):
        return (math.pi) * abs(self.radius * 2)


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2


def shape_info(shape):
    """Print area and perimeter of shape (duck typing)."""
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Permiter: {perimeter}")
