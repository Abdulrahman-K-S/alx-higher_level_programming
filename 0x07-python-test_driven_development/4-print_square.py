#!/usr/bin/python3
"""A module that prints a square with the character `#`.

This module prints a square out of `#`.

"""


def print_square(size):
    """Prints a square

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not of type integer.
        ValueError: If size is less than 0.

    """
    if type(size) not in (int, float):
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
