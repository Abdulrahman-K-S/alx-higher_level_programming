#!/usr/bin/python3
"""Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square

    The square class inherits from the rectangle class as
    it's a special rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        The class Square constructor.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__

        Updating the __str__ function
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        ))

    @property
    def size(self):
        """size

        Getter for the size attribute (aka width/height).
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update

        Updates the attributes of the Square class.
        """
        argc = len(args)
        kwargc = len(kwargs)
        attributes = ['id', 'size', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, attributes[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in attributes:
                    setattr(self, k, v)

    def to_dictionary(self):
        """to_dictionary

        Returns a dictionary of the Square class.
        """
        return ({
            'id' : self.id,
            'size' : self.size,
            'x' : self.x,
            'y' : self.y
        })
