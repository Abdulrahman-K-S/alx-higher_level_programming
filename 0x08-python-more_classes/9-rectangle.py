#!/usr/bin/python3
"""9. A square is a rectangle

This module defines a class Rectangle

"""


class Rectangle:
    """class Rectangle

    A class that has 2 private attributes (height & width).

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        number_of_instances (int): The number of instances of the class.
        print_symbol (any type): The symbol for printing

    """

    __width = None
    __height = None
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        The default class constructor.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints the rectangle

        Prints the rectangle using `print_symbol`

        Return:
            (string): The rectangle in `print_symbol`.

        """
        shape = ""
        if self.__height == 0 or self.__width == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                shape = shape + str(self.print_symbol)
            if i < (self.__height - 1):
                shape = shape + '\n'
        return shape

    def __repr__(self):
        """repr

        Returns a string representation of the rectangle.

        Return:
            (string): Represenation of the rectangle.

        """
        return ("Rectangle({:d}, {:d})".format(
            eval(str(self.__width)), eval(str(self.__height))))

    @property
    def width(self):
        """width getter

        Gets the width's value.

        Return:
            (int): The width.

        """
        return self.__width

    def __del__(self):
        """del

        The default class deconstructor.

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger or Equal

        Compares two rectangle classes to see if one is biiger
        or if they're equal to each other.

        Args:
            rect_1 (class <Rectangle>): First rectangle.
            rect_2 (class <Rectangle>): Second rectangle.

        Return:
            (class <Rectangle>): The bigger rectangle or rect_1 if
                                they're equal.

        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Square class method

        Creates a class of rectangle that has a width=height=size.
        Which makes it a square.

        Args:
            size (int): The size of the square sides.

        Return:
            (class <Rectangle>): With equal width & height.

        """
        return cls(size, size)
