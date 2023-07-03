#!/usr/bin/python3

"""this module houses a Rectangle class"""


class Rectangle:
    """
    This class is a rectangle class.

    Attributes:
        number_of_instances (int): The number of instances of rectangels.
        print_symbol (any): The symboly used to rep strings.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        init method for a new Rectangle.

        Args:
            width (int): This is the width of the rectangle.
            height (int): This is the height of the  rectangle.
        """
        type(self).number_of_instances += 1
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the Rectangle.

        Args:
            value (int): The width value to set.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
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
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for _ in range(self.__height):
            rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """
        Return a string representation of the Rectangle that can be used to recreate an instance.

        Returns:
            str: The string representation of the Rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
