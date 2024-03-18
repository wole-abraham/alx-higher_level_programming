#!/usr/bin/python3

def max_int(lists=[]):
    result = lists[0]

    i = 1

    while i < len(lists):
        if lists[i] > result:
            result =  lists[i]
        i += 1
    return result
listt = [6, 7, 10, 22, 55, 31]
print(max_int(listt))
