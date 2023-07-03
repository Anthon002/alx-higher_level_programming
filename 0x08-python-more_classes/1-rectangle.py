#!/usr/bin/python3
"""This module contains the Rectangle """

class Rectangle:
    """ This is the rectangle class """
    def __init__(self, width = 0, height = 0):
        """initializer for the rectangle

        Args:
            width(int): the width of the triangle
            height(int): thei height of the triangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        The getter function for the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        The setter method for the width
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        The getter funciton for the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        The setter function for the height
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
