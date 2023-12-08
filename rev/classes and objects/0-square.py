#!/usr/bin/python3

class Square:
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print(f"Hi there {self.name}")

p = Square("jake")
p.say_hi()
