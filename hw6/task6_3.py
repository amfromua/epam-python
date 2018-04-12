#!/usr/bin/env python3.6


def task6_3():
    """ Method that solves task6_3:
    takes number of integers and then displays the result of
    dividing the first number by the second

    :return: None
    """
    try:
        pair_number = int(input('Input number '))
    except TypeError as e:
        print('Error code: invalid literal for int() with base 10 \'{}\''.format(e))

    pairs = []

    for i in range(pair_number):

        pair = input().split()
        if len(pair) != 2:
            raise AssertionError('Wrong number of integers')
        pairs.append(pair)


    for i in range(pair_number):
        try:
            result = int(pairs[i][0]) // int(pairs[i][1])
            print(result)
        except (ZeroDivisionError, ValueError) as e:
            print('Error code: {}'.format(e))

if __name__ == "__main__":
    task6_3()