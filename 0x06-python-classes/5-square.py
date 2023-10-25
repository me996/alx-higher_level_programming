#!/usr/bin/python3
"""define a module."""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """consructor.
        Args:
            size: lenght of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """property for the lenght of a side of this square.
        Raises:
            TypeEroor: if size is not an integer.
            ValueError: if size is less than 0.
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
        """Area of this square.
        returns:
              the size sqaure.
        """
        return self.__size ** 2

    def my_print(self):
        """print this square."""
        for i in range ( self.size):
            for j in range(self.size):
                print('#', end="\n" if j is self.size - 1 and i != j else "")
         print()
