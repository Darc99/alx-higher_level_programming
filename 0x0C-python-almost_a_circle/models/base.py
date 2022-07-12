#!/usr/bin/python3
"""
This contains the base class
"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init the base class
        Attribute:
              id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

