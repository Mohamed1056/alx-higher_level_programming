#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")

    except IndexError:
        if (x > len(my_list)):
            x = len(my_list)
    print()
    return (x)
