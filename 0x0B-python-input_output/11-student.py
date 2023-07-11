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

    def to_json(self, attrs=None):
        """this function reps the students class in a dictionary format.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return json.loads(json.dumps(self.__dict__))
        
    def reload_from_json(self, json):
        """This function will  replace all attributes of the Student instance.
        """
        for i, j in json.items():
            setattr(self, i, j)
