#!/usr/bin/python3
'''
BaseGeometry module inhearted to the Rectangle class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    '''
    def __init__(self, width, height):
        '''Rectangle class constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''area

        Calculates the area of the rectangle.

        Return:
            (int): The area of the rectangle.
        '''
        return self.__width * self.__height

    def __str__(self):
        '''__str__

        Return:
            (str): The description of the Rectangle class.
        '''
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
