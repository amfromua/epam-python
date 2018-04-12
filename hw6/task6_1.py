#!/usr/bin/env python3.6


class Price:
    """Price descriptor"""

    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return instance.__dict__[self.label]

    def __set__(self, instance, value):
        if value not in range(0, 101):
            raise ValueError("Price must be between 0 and 100.")
        instance.__dict__[self.label] = value



class Book:
    """Class of book"""

    price = Price('price')

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


if __name__ == "__main__":
    b = Book('William Faulkner', 'The Sound and the Fury', 12)

    b.price = 22 # ok
    print(b.price)
    b.price = -1000 # ValueError


