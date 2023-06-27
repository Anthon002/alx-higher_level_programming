#!/usr/bin/python3

"""Experience the power of squares with the Square class."""


class Square:
    """Embark on an epic journey with the mighty Square."""

    def __init__(self, size=0):
        """Summon a new square into existence.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Unveil the current size of the square."""
        return self.__size

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
        self.__size = value

    def area(self):
        """Unleash the fury of the square's area.

        Returns:
            int: The almighty area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Manifest the square's grandeur by printing it with the # character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
