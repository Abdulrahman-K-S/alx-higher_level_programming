# #!/usr/bin/python3
"""A module that adds two numbers

This module performs the addition operation between two numbers
and the numbers could be either an integer or a float.

"""


def add_integer(a, b=98):
    """Adds two integers

    Performs the addition operation

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int: The result of the addition.

    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
