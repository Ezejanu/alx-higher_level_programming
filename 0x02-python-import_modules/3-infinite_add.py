#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    n = len(sys.argv)
    argv_sum = 0
    for i in range(1, n):
        argv_sum += int(sys.argv[i])
    print("{}" .format(argv_sum))
