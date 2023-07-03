#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """A rectangle is represented by this class.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

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
        """The width of the rectangle is obtained or set."""
        return self.__width

    @width.setter
    def width(self, value):
        """The width of the rectangle is set.

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
        """The height of the rectangle is obtained or set."""
        return self.__height

    @height.setter
    def height(self, value):
        """The height of the rectangle is set.

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
        """The area of the rectangle is calculated and returned.

        Returns:
            int: The area is calculated.
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """The perimeter of the rectangle is calculated and returned.

        Returns:
            int: The perimeter is calculated.
        """
        perimeter = 0
        while self.__width != 0 and self.__height != 0:
            perimeter = (self.__width * 2) + (self.__height * 2)
            return perimeter
        return perimeter

    def __str__(self):
        """A string representation of the rectangle is returned.

        Returns:
            str: The string representation is returned.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        therectangel = []
        i = 0
        while i < self.__height:
            therectangel.append("#" * self.__width)
            if i != self.__height - 1:
                therectangel.append("\n")
            i += 1

        return "".join(therectangel)

    def __repr__(self):
        """A string representation of the rectangle object is returned.

        Returns:
            str: The string representation is returned.
        """
        therectangel = f"Rectangle({self.__width}, {self.__height})"
        return therectangel

    def __del__(self):
        """A farewell message is printed upon deletion of the rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
