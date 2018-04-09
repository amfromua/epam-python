#!/usr/bin/env python3.6

from datetime import datetime



class Wine:
    """Create instance of Wine class

    """

    def __init__(self, name, mark, country, notation, date):
        """Create instance of Wine class

        :param name: str, name of wine
        :param mark: str, trademark of wine
        :param country: str, country manufacturer
        :param notation: str, notations
        :param date: date of creation
        """

        self.name = name
        self.mark = mark
        self.country = country
        self.date = date
        self.notation = notation

    def get_age(self):
        """Counts the difference between day of creation and today

        :return: number of days from day of creation
        """
        today = datetime.strptime(self.date,"%Y-%m-%d")
        return abs((today.date()-datetime.now().date()).days)



if __name__ == "__main__":
    vinovino = Wine(name='asdad', mark='213a', country='Estonia', notation='dsdddasdasdasda', date='2018-02-02')
    print(vinovino.get_age())

