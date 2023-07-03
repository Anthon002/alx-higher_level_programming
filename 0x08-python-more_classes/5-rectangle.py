#!/usr/bin/python3
"""Representation of a Rectangle."""


class Rectangle:
    """Class to represent a geometric rectangle shape."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the provided width is not an integer.
            ValueError: If the provided width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the provided height is not an integer.
            ValueError: If the provided height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The calculated area.
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The calculated perimeter.
        """
        perimeter = 0
        if self.__width != 0 and self.__height != 0:
            perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: The string representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        therectangle = []
        for _ in range(self.__height):
            therectangle.append("#" * self.__width)
            if _ != self.__height - 1:
                therectangle.append("\n")
        return "".join(therectangle)

    def __repr__(self):
        """Return a string representation of the rectangle object.

        Returns:
            str: The string representation.
        """
        therectangle = f"Rectangle({self.__width}, {self.__height})"
        return therectangle

    def __del__(self):
        """Print a farewell message upon deletion of the rectangle."""
        print("Bye rectangle...")
