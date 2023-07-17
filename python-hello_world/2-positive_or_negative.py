#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    print("{} is positive".format(str(number)))
elif (number == 0):
    print("{} is zero".format(str(number)))
else:
    print("{} is negative".format(str(number)))
