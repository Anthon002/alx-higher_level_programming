#!/usr/bin/python3

"""Implementation of a Square class."""


class Square:
    """Represents a square shape.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The side length of the square.
        """
        self.__size = size
