#!/usr/bin/python3
"""This module contains the load_from_json_file() function 
"""
import json


def load_from_json_file(filename):
    """ this funciton creates an object from a json file
    """
    with open(filename, 'r', encoding="utf-8") as the_file:
        return json.load(the_file)
