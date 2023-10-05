#!/usr/bin/python3
from sys import argv
def arguments(argv):
    no_args = len(argv) - 1

    if no_args == 0:
        print("{} arguments".format(no_args))
    elif no_args == 1:
        print("{} argument:".format(no_args))
        print("{}: {}".format(no_args, argv[1]))
    else:
        print("{} arguments:".format(no_args))
        for x in range(1, len(argv)):
            print("{}: {}".format(x, argv[x]))
if __name__ == "__main__":
    arguments(argv)
