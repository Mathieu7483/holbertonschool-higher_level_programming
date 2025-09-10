#!/usr/bin/python3
"""
Module to divide all elements of a matrix by a given divisor.
Validates input matrix and divisor, and returns a new matrix with
elements rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div, rounding to 2 decimals.
    Args:
        matrix (list of list of int/float): Input matrix.
        div (int/float): Divisor.
    Raises:
        TypeError: If matrix or div is invalid.
        ZeroDivisionError: If div is zero.
    Returns:
        new matrix with divided and rounded elements.
    """
    