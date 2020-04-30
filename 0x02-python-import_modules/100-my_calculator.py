#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    from calculator_1 import add, sub, mul, div
    if len(s.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ch = {"+" : add, "-" : sub, "*" : mul, "/" : div}
    if s.argv[2] not in ch:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    resulta = ch[s.argv[2]](int(s.argv[1]), int(s.argv[3]))
    print("{} {} {} = {}".format(s.argv[1], s.argv[2], s.argv[3], resulta))
