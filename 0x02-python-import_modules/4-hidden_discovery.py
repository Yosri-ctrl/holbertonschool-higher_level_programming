#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as h
    ch = dir(h)
    for i in range(len(ch)):
        if ch[0] != "_":
            print("{}".format(ch[i]))
