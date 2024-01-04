#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("1 argument:")
    else
        print("{} argument:".format(x))
    for n in range(x):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))

