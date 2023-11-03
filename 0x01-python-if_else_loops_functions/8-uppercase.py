#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) == 32:
            print(ch, end="")
        else:
            a = ord(ch) - 32
            print(f"{chr(a)}", end='')
