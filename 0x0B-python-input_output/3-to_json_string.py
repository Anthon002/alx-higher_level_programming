#!/usr/bin/python3
"""this module contains the to_json_string
"""
import json


def to_json_string(my_obj):
    """
    this function encodes my_obj to json
    """
    return(json.dumps(my_obj))
