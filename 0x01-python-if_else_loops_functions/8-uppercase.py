#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) == 32 or ord(ch) >= 65 and ord(ch) <= 90:
            print("{}".format(ch), end='')
        elif ord(ch) > 90:
            a = ord(ch) - 32
            print("{}".format(chr(a)), end='')
