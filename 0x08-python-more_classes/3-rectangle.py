#!/usr/bin/python3
""" This module contains the Rectangle class
"""
class Rectangle:
    """ the retangle class """
    def __init__(self, width=0, height=0):
        """ constructor that initializes optional width with height"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """ getter for width
        """
        return self._width

    @property
    def height(self):
        """ getter for height
        """
        return self._height

    @width.setter
    def width(self, value):
        """  setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @height.setter
    def height(self, value):
        """ setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """  area or rectangle method """
        return self._width * self._height

    def perimeter(self):
        """ rectangle perimiter method """
        if self._width == 0 or self._height == 0:
            return 0
        return self._width * 2 + self._height * 2

    def __str__(self):
        """ returns rectangle with the # char
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width for _ in range(self._height)])
