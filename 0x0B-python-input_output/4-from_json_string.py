#!/usr/bin/python3
"""this module contains the function from_json_string()
"""
import json

def from_json_string(my_str):
    """
    this fucntion returns the string to json format
    """
    return(json.loads(my_str))
