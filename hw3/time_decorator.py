#!/usr/bin/env python3


from datetime import *


def wrapper(some_function):
    """ Decorator that calculates
    time of execution of some function
    """


    def inner():
        start = datetime.now()
        some_function()
        finish = datetime.now()
        print(finish-start)
        return some_function
    return inner


@wrapper
def foo():
    """Just random function"""
    for i in range(1000):
        i**i*2*i + i**i*2*i

foo()
