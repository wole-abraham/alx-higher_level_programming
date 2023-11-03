#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(c) >= 97 and ord(c) <= 172:
            a = ord(ch) - 32
            print("{}".format(chr(a)), end='')
        else:
           print("{}".format(ch), end='')
