#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The position of the square, default is (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter to retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to set the position of the square with validation.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' considering the position."""
        if self.__size == 0:
            print("")
        else:
            # Print new lines based on the y position
            print("\n" * self.__position[1], end="")
            # Print the square with spaces for the x position
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
