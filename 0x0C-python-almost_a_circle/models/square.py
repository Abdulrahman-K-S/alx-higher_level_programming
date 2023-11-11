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
