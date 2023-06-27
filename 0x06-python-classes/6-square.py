#!/usr/bin/python3

"""Discover the power of squares with the Square class."""


class Square:
    """Unleash the potential of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Summon a new square into existence.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

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

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the provided position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """Print the square with the '#' character."""
        if self._size == 0:
            print()
            return

        for _ in range(self._position[1]):
            print()

        for _ in range(self._size):
            print(" " * self._position[0], end="")
            print("#" * self._size)
