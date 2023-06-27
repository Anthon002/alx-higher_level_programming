#!/usr/bin/python3

"""Unleash the power of squares with the Square class."""


class Square:
    """Witness the might of a perfect square."""

    def __init__(self, size=0):
        """Summon a new square into existence.

        Args:
            size (int): The size of the new square.
        """
        self._size = None
        self.size = size

    @property
    def size(self):
        """Unveil the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Harness the power to resize the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Unleash the fury of the square's area.

        Returns:
            int: The almighty area of the square.
        """
        return self._size ** 2
