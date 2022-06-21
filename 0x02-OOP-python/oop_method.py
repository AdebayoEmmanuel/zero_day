#!/usr/bin/python3
class Person:
    """Just playing around with OOP self and method
        according to python.swaroopch.com
    """
    def say_hi(self):
        print('Hello, how are you?')

p = Person()

p.say_hi() # same as Person().say_hi() (terrible practice, abstain)
