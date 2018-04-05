#!/usr/bin/env python3

import math

def convert(string):
    """Function that converts string to int number

    :alarm: don't put anything starts from '\' to function
    :param string: string
    :return:
    """

    if string:
        ord_value = ord(string[-1])
        number_of_digits = math.floor(math.log10(ord_value))+1 # counts number of digits in ord_value
        return ord_value + convert(string[:-1])*10**number_of_digits
    return 0
