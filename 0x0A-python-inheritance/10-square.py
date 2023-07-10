#!/usr/bin/python3
"""This module contains a Square class ."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is a square class that inherits from the rectangle class."""

    def __init__(self, size):
        """This initializer costructs a new square.

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
