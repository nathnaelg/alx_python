#!/usr/bin/python3
"""
Finds if the object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """if object is an instance of a class that
    inherited from a class.
    Args:
        - obj: object to look at
        - a_class: class to evaluate
    Returns: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
