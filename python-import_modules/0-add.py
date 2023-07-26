#!/usr/bin/python3
from add_0 import add

# define variables
a = 1
b = 2


# call the main function
def main():
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result), end="\n")

if __name__ == "__main__":
    main()