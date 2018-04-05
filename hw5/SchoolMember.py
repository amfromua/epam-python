#!/usr/bin/env python3

class SchoolMember:
    '''Base class for everybody in school'''

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    '''Class derived from SchoolMember class'''

    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)

    def show(self):
        '''Method that prints name, age and salary of a teacher'''

        print('Имя: "{name}" Возраст:"{age}" Зарплата: "{salary}"'.format(name=self.name, age=self.age, salary=self.salary))


class Student(SchoolMember):
    '''Class derived from SchoolMember class'''

    def __init__(self, name, age, marks):
        self.marks = marks
        super().__init__(name, age)

    def show(self):
        '''Method that prints name, age and marks of a student'''

        print('Имя: "{name}" Возраст: "{age}" Оценки: "{marks}"'.format(name=self.name, age=self.age, marks=self.marks))


if __name__ == "__main__":
    persons = [Teacher('Mr.Poopybutthole', 40, 3000), Student('Morty', 16, 75)]
    for pers in persons:
        pers.show()
