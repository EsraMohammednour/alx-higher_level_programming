#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        print(f"{x} arguments.")
    elif x == 1:
        print(f"{x} argument:")
    else:
        print("{} arguments:".format(x))
    for i in range(x):
        print(f"{i + 1}: {sys.argv[i + 1]}")
