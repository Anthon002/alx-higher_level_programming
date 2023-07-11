#!/usr/bin/python3
"""This module loads and save add_item.json."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        the_elements = load_from_json_file("add_item.json")
    except FileNotFoundError:
        the_elements = []
    items.extend(sys.argv[1:])
    save_to_json_file(the_elements, "add_item.json")
