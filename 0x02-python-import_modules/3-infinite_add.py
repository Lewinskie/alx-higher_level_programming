#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("0".format())
    else:
        sum = 0
        for args in argv[1:]:
            sum += int(args)
        print("{}".format(sum))
