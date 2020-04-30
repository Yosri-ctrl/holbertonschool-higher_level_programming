#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    if len(s.argv) == 1:
        print("0 arguments.")
    elif len(s.argv) == 2:
        print("1 argument:")
        print("1: {}".format((s.argv[1])))
    else:
        print("{} arguments:".format(len(s.argv) - 1))
        for i in range(1, len(s.argv)):
            print("{}: {}".format(i, s.argv[i]))
