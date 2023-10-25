#!/usr/bin/python3
"""square module."""


class Square:
    """define a square."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size: lenght of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """property for the lenght of a sode of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
       """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
