#!/usr/bin/python3
"""A square class"""


class Square:
    """
    This class defines a square class

    Attributes:
        __size (int): The size of the square.
    """
    __size = None

    def __init__(self, size=0):
        """__init__

        The __init__ method initalizes the size value
        of the square (constructor)

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """area

        Returns the current area of the square
        """
        return self.__size ** 2
