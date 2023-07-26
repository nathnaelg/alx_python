#!/usr/bin/python3


# define raise_exception fucnction
def raise_exception():
    try:
        raise TypeError()
    except TypeError as te:
        raise te
