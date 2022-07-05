#!/usr/bin/python3
"""defining the function lookup that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """returns list object"""
    return dir(obj)
