#!/usr/bin/python3
"""this module saves and load json file
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__("save_to_json_file.py").save_to_json_file
    load_from_json_file = __import__("load_from_json_file.py").load_from_json_file
    try:
        items = load_from_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.arg[:1])
    save_to_json_file(items, "add_item.json")
