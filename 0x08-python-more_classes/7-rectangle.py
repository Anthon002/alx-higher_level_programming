#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """A rectangle is represented by this class.

    Attributes:
        number_of_instances (int): The number of instances of the Rectangle.
        print_symbol (any): The symbol used for the string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """A new Rectangle instance is initialized.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the provided width is not an integer.
            ValueError: If the provided width is negative.
        """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the provided height is not an integer.
            ValueError: If the provided height is negative.
        """
        if not type(value) == int:
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
        while self.__width != 0 and self.__height != 0:
            perimeter = (self.__width * 2) + (self.__height * 2)
            return perimeter
        return perimeter

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: The string representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        therectangel = []
        i = 0
        while i < self.__height:
            therectangel.append(str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                therectangel.append("\n")
            i += 1

        return "".join(therectangel)

    def __repr__(self):
        """Return a string representation of the rectangle object.

        Returns:
            str: The string representation.
        """
        therectangel = f"Rectangle({self.__width}, {self.__height})"
        return therectangel

    def __del__(self):
        """Print a farewell message upon deletion of the rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
