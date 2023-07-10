#!/usr/bin/python3

"""this module contains a class MyList and a print_sorted() function """

class MyList(list):
    """ This class inherits from the list class """
    def print_sorted(self):
        """
        This function prints out a list 
        Arg:
            self: self
        Return: nothing
        """
        sorted_list = sorted(self)
        print(sorted_list)
