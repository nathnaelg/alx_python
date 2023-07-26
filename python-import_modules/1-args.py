#!/usr/bin/python3
import sys


def main():
    # get number of arguments
    num = len(sys.argv) - 1
    # if no argument
    if num == 0:
        end_char = ".\n"
        # print 0 arguments.
        print("{} arguments".format(num), end=end_char)
    # if one argument
    elif num == 1:
        end_char = ":\n"
        # print 1 argument:
        print("{} argument".format(num), end=end_char)
    # else if more than one argument
    else:
        end_char = ":\n"
        # print <number of arguments>:
        print("{} arguments".format(num), end=end_char)
    # iterate through the total number of arguments
    for i in range(1, num + 1):
        # print the index of argument, followed by the argument
        print("{}: {}".format(i, sys.argv[i]), end="\n")

if __name__ == "__main__":
    main()
