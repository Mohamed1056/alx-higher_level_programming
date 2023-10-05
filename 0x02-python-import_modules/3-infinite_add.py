#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(int(sys.argv[1:])):
        sum += i
    print(sum)
