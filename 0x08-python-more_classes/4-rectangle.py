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

    def __str__(self):
        """Prints the rectangle

        Prints the rectangle using '#'

        Return:
            (string): The rectangle in '#'.

        """
        shape = ""
        if self.__height == 0 or self.__width == 0:
            return ''
        for i in range(self.__height):
            for i in range(self.__width):
                shape = shape + '#'
            if i < (self.__height - 1):
                shape = shape + '\n'
        return shape

    def __repr__(self):
        """repr

        Returns a string representation of the rectangle.

        Return:
            (string): Represenation of the rectangle.

        """
        return ("Rectangle({}, {})".format(
            eval(str(self.__width)), eval(str(self.__height))))

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

    def area(self):
        """area

        Calculates the area of the rectangle & returns it.

        Return:
            (int): The area of the rectangle.

        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter

        Calculates the perimeter of the rectangle & returns it.

        Return:
            (int): The perimeter of the rectangle.

        """
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)
