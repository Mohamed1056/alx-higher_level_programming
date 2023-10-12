#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    summ = 0
    for i in range(len(my_list)):
        mul = my_list[i][0] * my_list[i][1]
        fum = my_list[i][1]
        num += mul
        summ += fum
    return (num / summ)
