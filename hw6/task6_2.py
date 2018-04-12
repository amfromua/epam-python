#!/usr/bin/env python3.6

import abc


class Vehicle(metaclass=abc.ABCMeta):
    """ Abstract base vehicle class"""

    def __init__(self, trademark, year, basic_price, mileage, wheels):
        self.year = year
        self.mileage = mileage
        self.wheels = wheels
        self.trademark = trademark
        self.basic_price = basic_price

    @classmethod
    def vehicle_type(cls):
        """Return vehicle type

        :param cls: class
        :type cls: class
        :return: class name
        :rtype: str
        """
        return cls.__name__


    def is_motorcycle(self):
        """Return true if vehicle is motorcycle and false otherwise"""

        if self.wheels == 2:
            return True
        return False


    def purchase_price(self):
        """ Function that returns current price of some vehicle

        :return: price of *some vehicle
        :rtype: float
        """

        return self.basic_price - 0.1*self.mileage


class Car(Vehicle):
    def __init__(self, trademark, year, basic_price, mileage):
        super().__init__(trademark, year, basic_price, mileage, 4)



class Motorcycle(Vehicle):
    def __init__(self, trademark, year, basic_price, mileage):
        super().__init__(trademark, year, basic_price, mileage, 2)



class Truck(Vehicle):
    def __init__(self, trademark, year, basic_price, mileage):
        super().__init__(trademark, year, basic_price, mileage, 8)



class Bus(Vehicle):
    def __init__(self, trademark, year, basic_price, mileage):
        super().__init__(trademark, year, basic_price, mileage, 6)



if __name__ == "__main__":
    car = Car('Subary', 1967, 9_000, 6_000)
    motorcycle = Motorcycle('Subary', 1967, 12_000, 6_000)
    truck = Truck('KAMAZ',  1977, 1_000_000, 100_000)
    bus = Bus('MAZ',  2_000, 920_000, 50_000)

    vehicles = [car, motorcycle, truck, bus]
    for v in vehicles:
        print('Info about {}'.format(v.vehicle_type()))
        print('Is it a motorcycle? - {vtype}. What\'s the price? - {price}'\
              .format(vtype=v.is_motorcycle(), price=v.purchase_price()))
        print('----------')