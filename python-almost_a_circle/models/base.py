#!/usr/bin/python3
"""Defines Base class """


class Base:
    """Class Base.

    Attributes:
        id (int): Identity of each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Creates instances of Base.

        Args:
            id (int, optional): Identity of instance.
        """
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
