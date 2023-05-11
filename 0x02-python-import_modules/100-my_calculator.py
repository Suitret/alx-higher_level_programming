#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if argv[1] not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(argv[0])
            b = int(argv[2])
            op = argv[1]

            if op == '+':
                print(a, op, b, "=", add(a, b))
            elif op == '-':
                print(a, op, b, "=", sub(a, b))
            elif op == '*':
                print(a, op, b, "=", mul(a, b))
            else:
                print(a, op, b, "=", div(a, b))
