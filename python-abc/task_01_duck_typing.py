#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius=0):
        Circle.radius = radius

    def area(self):
        return (math.pi)*(Circle.radius**2)
    
    def perimeter(self):
        return (math.pi) * (Circle.radius * 2)

class Rectangle(Shape):
    def __init__(self, height, width):
        Rectangle.height = height
        Rectangle.width = width

    def area(self):
        return Rectangle.height * Rectangle.width
    
    def perimeter(self):
        return (Rectangle.height * 2) +(Rectangle.width * 2)

def shape_info(shape):
    area = shape.area() 
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Permiter: {perimeter}")
