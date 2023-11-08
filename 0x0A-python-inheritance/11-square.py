#!/usr/bin/python3
'''
Rectangle module inhearted to the Square class
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square

    Attributes:
        __size (int): The size of the square.
    '''
    def __init__(self, size):
        '''The Square class constructor'''
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''__str__

        Return:
            (str): The description of the Square class.
        '''
        return ("[Square] {}/{}".format(self.__size, self.__size))
