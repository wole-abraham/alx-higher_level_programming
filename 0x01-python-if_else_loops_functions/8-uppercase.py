#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 172:
            a = ord(ch) - 32
            print("{}".format(chr(a)), end='')
        else:
           print("{}".format(ch), end='')
