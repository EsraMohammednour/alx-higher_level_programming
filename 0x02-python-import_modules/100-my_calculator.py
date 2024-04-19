#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1.py import add, sub, mul,div
    if len(sys.argv) - 1 != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    o = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(o.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    print(f"{a} {sys.argv[2]} {b} = {o[sys.argv[2]](a, b)}")
