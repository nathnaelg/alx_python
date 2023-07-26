#!/usr/bin/python3


# define function that removes character 'C', 'c' in a string
def no_c(my_string):
    result = ""
    for char in my_string:
        if char != "c" and char != "C":
            result += char
    return result
