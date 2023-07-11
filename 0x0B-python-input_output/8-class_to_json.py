#!/usr/bin/python3
"""this module contains a  class-to-JSON() function."""


def class_to_json(obj):
    """this fuction returns the object as a dict."""
    return obj.__dict__
