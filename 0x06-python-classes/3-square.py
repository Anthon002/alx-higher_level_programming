#!/usr/bin/python3
"""
Welcome to the world of squares! This module defines a Square class that represents
the essence of square-shaped awesomeness.
"""


class Square:
    """
    Behold, the magnificent Square!

    Attributes:
        __size (int): The size of the Square, defining its magical powers.
    """

    def __init__(self, size=0):
        """
        Summon a new Square into existence!

        Args:
            size (int): The size of the new Square.
        """
        self.__size = self.__validate_size(size)

    def __validate_size(self, size):
        """
        Validate the size value and unleash the powers of the Square.

        Args:
            size (int): The size of the Square.

        Returns:
            int: The validated size value, now ready for epic adventures.

        Raises:
            TypeError: If the size is not an integer, for that's the Square's code.
            ValueError: If the size is less than 0, for positivity fuels the Square's magic.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer, for Square's sake!")
        elif size < 0:
            raise ValueError("size must be >= 0, or else the Square's power shall wane!")
        return size

    def area(self):
        """
        Unleash the Square's mystical area, revealing its hidden powers.

        Returns:
            int: The area of the Square, the embodiment of its awe-inspiring might.
        """
        return self.__size ** 2
