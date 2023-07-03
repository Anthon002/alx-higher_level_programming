#!/usr/bin/python3
"""Rectangle class that represents a geometric rectangle shape."""

class Rectangle:
    """A geometric rectangle shape is represented by this class."""
    def __init__(self, width=0, height=0):
        """A new Rectangle instance is initialized.
    
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """The width of the rectangle is gotten or set."""
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
        """The height of the rectangle is gotten or set."""
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
        while self.__width != 0 and self.__height != 0:
            perimeter = (self.__width * 2) + (self.__height * 2)
            return perimeter
        return 0
    
    def __str__(self):
        """A string representation of the rectangle is returned.
    
        Returns:
            str: The string representation is returned.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
    
        therectangle = []
        i = 0
        while i < self.__height:
            therectangle.append("#" * self.__width)
            if i != self.__height - 1:
                therectangle.append("\n")
            i += 1
    
        return "".join(therectangle)
    
    def __repr__(self):
        """A string representation of the rectangle object is returned.
    
        Returns:
            str: The string representation is returned.
        """
        therectangle = f"Rectangle({self.__width}, {self.__height})"
        return therectangle
