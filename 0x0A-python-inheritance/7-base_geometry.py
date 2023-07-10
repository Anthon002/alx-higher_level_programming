#!/usr/bin/python3
"""This class contains the BaseGeometry class
"""


class BaseGeometry:
    """This is the Base Geometry class
    """

    def area(self):
        """This method raises and exception
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ this is the integer validator method 
        
        Args:
            name (str): name of parameter
            value (int): parameter to be validated

        Raises:
            TypeError: if the value is not an int
            ValueError: if the value is less than 0

        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
