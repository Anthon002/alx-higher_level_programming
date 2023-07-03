#!/usr/bin/python3
"""A Rectangle class is defined."""

class Rectangle:
    """A rectangle is represented
    Attributes:
        number_of_instances (int): The number of instances of Rectangle.
        print_symbol (any): The symbol used for string representation.
    """
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """A new Rectangle is initialized.
    
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """The width of the Rectangle is obtained or set."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError("width must be set to an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """The height of the Rectangle is obtained or set."""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError("height must be set to an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """The area of the Rectangle is returned."""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """The perimeter of the Rectangle is returned."""
        while self.__width != 0 and self.__height != 0:
            return ((self.__width * 2) + (self.__height * 2))
        return (0)
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """The Rectangle with the greater area is returned.
    
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If neither rect_1 nor rect_2 is an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
    
    @classmethod
    def square(cls, size=0):
        """A new Rectangle with width and height equal to size is returned.
    
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return cls(size, size)
    
    def __str__(self):
        """The printable representation of the Rectangle is returned.
    
        The Rectangle is represented with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        i = 0
        while i < self.__height:
            j = 0
            while j < self.__width:
                rect.append(str(self.print_symbol))
                j += 1
            if i != self.__height - 1:
                rect.append("\n")
            i += 1
        return "".join(rect)
    
    def __repr__(self):
        """The string representation of the Rectangle is returned."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect
    
    def __del__(self):
        """A message is printed for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
