#!/usr/bin/python3
"""A square class"""


class Square:
    """class Square

    This class defines a square class

    Attributes:
        __size (int): The size of the square.
    """
    __size = None
    
    def __init__(self, size):
        """__init__

        The __init__ method initalizes the size value
        of the square (constructor)
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
