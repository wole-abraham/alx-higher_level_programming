#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print(0, end='')
    elif number < 0:
        tf = (number * -1) % 10
        print(tf, end='')
    else:
        print(number % 10, end='')
