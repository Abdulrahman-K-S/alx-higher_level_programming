#!/usr/bin/python3
''' class MyInt that inherits from int '''


class MyInt(int):
    '''class MyInt

    MyInt is a rebel. MyInt has == and
    != operators inverted
    '''
    def __init__(self, number):
        '''The MyInt class constructor'''
        self.number = number

    def __eq__(self, other):
        '''__eq__

        The equal operator to be inverted.
        '''
        if self.number == int(other):
            return False
        return True

    def __ne__(self, other):
        '''__ne__

        The not-equal operator to be inverted.
        '''
        if self.number != int(other):
            return False
        return True
