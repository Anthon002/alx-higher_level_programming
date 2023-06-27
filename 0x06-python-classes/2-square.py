#!/usr/bin/python3
"""
This module defines a Square class representing a square shape.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The side length of the square.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The side length of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
