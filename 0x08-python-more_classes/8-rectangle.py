#!/usr/bin/python3

"""This module houses a Rectangle class."""


class Rectangle:
    """
    This class represents a rectangle.

    Attributes:
        number_of_instances (int): The number of instances of rectangles.
        print_symbol (any): The symbol used to represent strings.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the Rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the Rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.

        Returns:
            int: The calculated area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the Rectangle.

        Returns:
            int: The calculated perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the bigger one based on the area.

        Args:
            rect_1 (Rectangle): Rectangle 1.
            rect_2 (Rectangle): Rectangle 2.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The bigger rectangle.
        """
        if not type(rect_1) == Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) == Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
            str: The string representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        i = 0
        while i < self.__height:
            rect.append(str(self.print_symbol) * self.__width)
            i += 1
        return "\n".join(rect)

    def __repr__(self):
        """
        Return a string representation of the Rectangle object.

        Returns:
            str: The string representation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a farewell message upon deletion of the Rectangle instance."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
