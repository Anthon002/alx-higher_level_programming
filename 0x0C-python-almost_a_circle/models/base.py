#!/usr/bin/python3
""" this module contains the Base class
"""


class Base:
    """ this is the Base class """
    __nb_objects = 0
    def __init__(self, id = None):
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
