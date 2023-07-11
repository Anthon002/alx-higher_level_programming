#!/usr/bin/python3
"""this module contains the funciton save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """this function saves the my_obj obj as json to filename
    """
    with open(filename, 'w', encoding='utf-8') as the_file:
        json.dump(my_obj, the_file)
