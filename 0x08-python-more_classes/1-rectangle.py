#!/usr/bin/python3
"""01. Real definition of a rectangle

This module defines a class Rectangle that has private
width & height attributes

"""


class Rectangle:
    """class Rectangle

    A class that has 2 private attributes (height & width).

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    """

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        The default class constructor.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """

        __width = None
        __height = None

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter

        Gets the width's value.

        Return:
            (int): The width.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Sets the width's value.

        Args:
            value (int): The value to be assigned to the width.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter

        Gets the height's value.

        Return:
            (int): The height.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Sets the height's value.

        Args:
            value (int): The value to be assigned to the height.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
