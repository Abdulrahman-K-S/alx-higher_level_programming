#!/usr/bin/python3
"""A module that prints `My name is <first name> <last name>`

This module prints a promt `My name is <first name> <last name>`
where the `first name` & `last name` are inputed to the function.

"""


def say_my_name(first_name, last_name=""):
    """Prints the <first name> <last name>

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError:
            - If the first name is not of type `str`.
            - If the last name is not of type `str`.

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
