#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    t = 0
    for x in range(len(sys.argv) - 1):
        t += int(sys.argv[x + 1])
    print(t)
