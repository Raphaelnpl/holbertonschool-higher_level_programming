#!/usr/bin/python3
# 4-square.py
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square, default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the size of the square with validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
    