#!/usr/bin/python3
# 1-square.py
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square with a private instance attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
