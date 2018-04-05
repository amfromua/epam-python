#!/usr/bin/env python3

def validate(low_bound: int, upper_bound: int):
    """Decorator that validates values for a pixel

    :param low_bound: int
    :param upper_bound: int, should be less than low_bound
    :return:
    """
    def decorator(function):
        def wrapper(*args):
            if all(number in range(low_bound,upper_bound) for number in [*args]):
                function(*args)
            else:
                print("Function call is not valid!")
        return wrapper
    return decorator

@validate(0,256)
def set_pixel(r, g, b):
    """Function that gets 3 int arguments

    :param r: for red
    :param g: for green
    :param b: for blue
    :return:
    """
    print("Pixel created!")


set_pixel(12,2,3)
set_pixel(123123,423,44)

