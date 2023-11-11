#!/usr/bin/python3
"""Rectangle Module"""


from models.base import Base

class Rectangle(Base):
    """class Rectangle

    A rectangle class that inherits from the base class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x position of the rectangle.
        __y (int): The y position of the rectangle.
    """

    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The rectangle constructor
        """
        super().__init__(id)

        self.check_parameter(width, 'width')
        self.check_parameter(height, 'height')
        self.check_parameter(x, 'x')
        self.check_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width

        Getter function for the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.check_parameter(value, 'width')
        self.__width = value

    @property
    def height(self):
        """height

        Getter function for the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.check_parameter(value, 'height')
        self.__height = value

    @property
    def x(self):
        """x

        Getter function for the x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.check_parameter(value, 'x')
        self.__x = value

    @property
    def y(self):
        """y

        Getter function for the y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.check_parameter(value, 'y')
        self.__y = value

    def check_parameter(self, value, param):
        """check_parameter

        Checks whether the paramter is valued or not. If not
        raises an exception.

        Raises:
            TypeError: If the value is not of type `int`.
            ValueError:
                ('width', 'height'): If they're less than or equal to 0.
                ('x', 'y'): If they're less than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(param))
        if value <= 0 and param in ('width', 'height'):
            raise ValueError("{} must be > 0".format(param))
        if value < 0 and param in ('x', 'y'):
            raise ValueError("{} must be >= 0".format(param))

    def area(self):
        """area

        Returns the area of the rectangle.

        Returns:
            (int): The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """display

        Prints in stdout the Rectangle instance with the character `#`
        """
        if self.y > 0:
            print('\n' * self.y, end='')

        for i in range(self.height):
            if self.x > 0:
                print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """__str__

        Updating the __str__ function
        """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height
        ))

    def update(self, *args):
        """update

        Updates the attributes of the Rectangle class.
        """
        argc = len(args)
        attributes = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, attributes[i], args[i])
