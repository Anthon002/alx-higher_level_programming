#!/usr/bin/python3
"""
this module contains the square class 
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    this is a class Square the inherits from the class BaseGeometry
    """
    def __init__(self, size):
        """"
        Initialztion function for the class Square

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        magic method to return width or height

        Returns:
            width or height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        This method calculates the squares ara
        """
        the_area = self.__size ** 2
        return (the_area)
