#!/usr/bin/python3
for i in range(99):
    print("{:2d} = 0x{}".format(i, hex(i)[2:]).lstrip())
