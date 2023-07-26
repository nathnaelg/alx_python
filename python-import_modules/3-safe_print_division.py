#!/usr/bin/python3


# function definition
def safe_print_division(a, b):
    # declare a and b variables
    a, b
    # try perform division of two integers
    try:
        result = a / b
    # if b=0 raise a zerodivisionerror that prints none as a result
    except ZeroDivisionError:
        result = None
    # finally print inside result and return result
    finally:
        print("Inside result: {}".format(result))
    return result
