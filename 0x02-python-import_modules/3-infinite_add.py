#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    somme = 0
    for i in range(1, len(s.argv)):
        somme += int(s.argv[i])
    print("{}".format(somme))
