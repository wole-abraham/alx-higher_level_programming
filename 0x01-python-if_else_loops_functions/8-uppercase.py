#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) == 32:
            print("{}".format(ch), end='')
        else:
            a = ord(ch) - 32
            print("{}".format(chr(a)), end='')
