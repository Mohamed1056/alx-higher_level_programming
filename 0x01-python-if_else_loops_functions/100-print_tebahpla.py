#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2) == 0:
        i = chr(i)
    else:
        i = chr(i - 32)
    print("{}".format(i), end="")
