#!/usr/bin/env python3.6

class prop():
    def __init__(self, fget=None, fset=None, fdel=None):
        """ Create instance of prop

        :param fget: method that gets value
        :param fset: method that sets value
        :param fdel: method that deletes value
        """

        self.fget = fget
        self.fset = fset
        self.fdel = fdel


    def __get__(self, instance, instance_type=None):
        if instance is None:
            return self
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


    def getter(self, fget):
        """ Method to assign getter function
        :param fget: property getter
        :type fget: function
        """

        self.fget = fget


    def setter(self, fset):
        """ Method to assign setter function
        :param fset: property setter
        :type fset: function
        """

        self.fset = fset

    def deleter(self, fdel):
        """ Method to assign deleter function
        :param fdel: property deleter
        :type fdel: function
        """

        self.fdel = fdel



class Something:
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def attr_setter(self, update):
        self.x = update


if __name__ == '__main__':
    s = Something(3)
    print(s.attr)

    s.attr = 12
    print(s.attr)