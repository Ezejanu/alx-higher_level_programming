#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("{:d} arguments.".format(n))
    elif n == 1:
        print("{:d} argument:\n1: {}".format(n, sys.argv[n]))
    elif n > 1:
        print("{:d} arguments:".format(n))
        for i in range(1, n + 1):
            print("{}: {}".format(i, sys.argv[i]))
