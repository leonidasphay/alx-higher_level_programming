#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opcs = {'+': add,
            '-': sub,
            '*': mul,
            '/': div}
    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]

    for i in opcs:
        if i == sign:
            res = opcs[i](a, b)
            print("{:d} {:} {:d} = {:d}".format(a, i, b, res))
            exit(0)

print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

if __name__ == "__main__":
    main()
