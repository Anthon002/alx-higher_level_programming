#!/usr/bin/python3
""" This module contains the Rectangle class
"""

from models.base import Base

class Rectangle(Base):
    """ This is the rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the init function

        Args:
            width(int): width
            height(int): height
            x(int): x coordinates
            y(int): y coordinates
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter funciton ofr width """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter function for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Setter and getter for the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Setter and getter the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This method calcs the ara of the rectangle"""
        the_area = self.width * self.height
        return (the_area)

    def display(self):
        """ show the rectangle """
        if self.height == 0 or self.width == 0:
            print("")
            return

        for i in range(self.y):
                print("")
        for j in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for l in range(self.width):
                print("#",end="")
            print("")


    def update(self, *args, **kwargs):
    """Update the Rectangle.

    Args:
        *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents width attribute
            - 3rd argument represent height attribute
            - 4th argument represents x attribute
            - 5th argument represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
    """
    if args and len(args) != 0:
        a = 0
        while a < len(args):
            arg = args[a]
            if a == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif a == 1:
                self.width = arg
            elif a == 2:
                self.height = arg
            elif a == 3:
                self.x = arg
            elif a == 4:
                self.y = arg
            a += 1

    elif kwargs and len(kwargs) != 0:
        keys = list(kwargs.keys())
        i = 0
        while i < len(keys):
            k = keys[i]
            v = kwargs[k]
            if k == "id":
                if v is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = v
            elif k == "width":
                self.width = v
            elif k == "height":
                self.height = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v
            i += 1

    def __str__(self):
        """returns the info about rectangle in this format"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
