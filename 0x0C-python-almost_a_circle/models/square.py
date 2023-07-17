#!/usr/bin/python3
""" This module contins a square class that inherits from the rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the class square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initi function for the square class.

        Args:
            size (int): size of the Square objects.
            x (int): x coordinate of the square obj.
            y (int): x coordinate of the square obj.
            id (int):identity f the square obj.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter function of the size of the Square obj."""
        self_width = self.width
        return self_width

    @size.setter
    def size(self, value):
        """ Setter function of the size of the Squre obj"""
        self.width = value
        self.height = value

def update(self, *args, **kwargs):
    """ method to update the Square.

    Args:
        *args (ints): New attribute values.
            - First arg represents id attribute
            - Second arg represents size attribute
            - Third arg represents x attribute
            - Fourth arg represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
    """
    if args and len(args) != 0:
        a = 0
        num_args = len(args)
        while a < num_args:
            arg = args[a]
            if a == 0:
                if arg is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = arg
            elif a == 1:
                self.size = arg
            elif a == 2:
                self.x = arg
            elif a == 3:
                self.y = arg
            a += 1

    elif kwargs and len(kwargs) != 0:
        keys = list(kwargs.keys())
        num_kwargs = len(keys)
        b = 0
        while b < num_kwargs:
            k = keys[b]
            v = kwargs[k]
            if k == "id":
                if v is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = v
            elif k == "size":
                self.size = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v
            b += 1

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
