#!/usr/bin/python3
"""A module that prints a text

This module prints a long string with 2 new lines
after each of these characters: `.`, `?` and `:`.

"""


def text_indentation(text):
    """Prints text with indentation

    Args:
        text (str): The text to print with indentation.

    Raises:
        TypeError: If the text is not of type string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in ('.', '?', ':'):
            print("{}\n".format(text[i]))
        elif text[i - 1] in ('.', '?', ':'):
            continue
        else:
            print(text[i], end="")
