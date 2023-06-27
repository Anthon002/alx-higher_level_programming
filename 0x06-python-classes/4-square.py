#!/usr/bin/python3

"""
Welcome to the world of squares! 🎉 This module defines a Square class that represents
the incredible power of geometrical perfection.
"""


class Square:
    """
    Behold, the mighty Square! 🟦

    Attributes:
        __size (int): The size of the Square, shaping its awe-inspiring might.
    """

    def __init__(self, size=0):
        """
        Summon a new Square into existence! 🪄✨

        Args:
            size (int): The size of the new Square.
        """
        self.__size = self.__validate_size(size)

    def __validate_size(self, size):
        """
        Validate the size value and unlock the Square's hidden potential. 🔐

        Args:
            size (int): The size of the Square.

        Returns:
            int: The validated size value, now ready for monumental achievements.

        Raises:
            TypeError: If the size is not an integer, for squares are precise creatures.
            ValueError: If the size is less than 0, for squares thrive on positivity.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer, for squares seek perfection!")
        elif size < 0:
            raise ValueError("size must be >= 0, or else the Square's magic shall fade!")
        return size

    def area(self):
        """
        Unleash the Square's majestic area, revealing its true magnificence. 🌟

        Returns:
            int: The area of the Square, the embodiment of its timeless grandeur.
        """
        return self.__size ** 2
