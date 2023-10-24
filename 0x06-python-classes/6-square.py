#!/usr/bin/python3
"""A square class"""


class Square:
    """
    This class defines a square class

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        The __init__ method initalizes the size value
        of the square (constructor)

        Args:
            size (int): The size of the square.
            poistion (tuple): The position of the square.

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2 or type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        """size setter

        The setter property for size

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        """position setter

        Args:
            position: The position of the square.

        Raises:
            TypeError: If the tuple has negative numbers.
        """
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2 or type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        """area

        Returns the current area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#'

        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for i in range(self.__size):
                    print('#', end='')
                print()
