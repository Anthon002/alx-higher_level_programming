#!/usr/bin/python3
"""this module contains the rectangle subclass
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This Rectangle class inherits from the  BaseGeometry class"""
    def __init__(self, width, height):
        """constructor for the Rectangel class
        Args: 
            width(int):width
            height(int):int
        """
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        """area method that returns width * height
        """
        the_area = self.__width * self.__height
        return(the_area)
    def __str__(self):
        """string magic method
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
