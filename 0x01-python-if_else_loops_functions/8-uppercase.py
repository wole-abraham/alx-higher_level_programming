#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 172:
            a = ord(ch) - 32
            result += chr(a)
        else:
            result += ch
    print("{}".format(result))
