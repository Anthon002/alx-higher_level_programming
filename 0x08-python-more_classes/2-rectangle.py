#!/usr/bin/python3

""" This module has the area and perimeter methods """

class Rectangle:
    """ This is the rectangel class """
    def __init__(self, width = 0, height = 0):
        """ This is the constructor 
        
        Args: 
            width(int): The int width
            height(int): The int height

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
    
    def area(self):
        """
        This method calcs the area of a rectangle
        """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return(self.__width * self.__height)
    def perimeter(self):
        """
        This method calcs the perimeter of a rectangle
        """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            p = 2 * (self.__width + self.__height)
            return (p)
