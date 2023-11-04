#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        tf = 0
        print(tf, end='')
    elif number < 0:
        tf = (number * -1) % 10
        print(tf, end='')
    else:
        tf = number % 10
        print(tf, end='')
    return tf
