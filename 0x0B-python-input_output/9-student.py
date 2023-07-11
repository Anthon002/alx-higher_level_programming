#!/usr/bin/python3
"""This module defines a class student."""


class Student:
    """this class defines a new student."""

    def __init__(self, first_name, last_name, age):
        """this is the initializer for the student class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """represents the students in a dict format."""
        return self.__dict__
