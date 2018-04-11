#!/usr/bin/env python3.6


def get_data():
    """Function that returns data

    :return: set of courses
    """

    return [
        {'name': 'Anton', 'rate': 2, 'course': 'Python'},
        {'name': 'Bogdan', 'rate': 3, 'course': 'Python'},
        {'name': 'Artem', 'rate': 22, 'course': 'Java'},
        {'name': 'Erofey', 'rate': 212313, 'course': 'Java'},
        {'name': 'Oksana', 'rate': 12, 'course': 'Python'},
        {'name': 'Fedor', 'rate': 1, 'course': 'Python'},
        {'name': 'Paver', 'rate': 2, 'course': 'Python'},
        {'name': 'Kirill', 'rate': 21, 'course': 'Java'}
    ]


def get_courses(data):
    """Function that selects courses and returns them

    :param data: list of dicts
    :return: set of courses
    """

    return {item['course'] for item in data}


def get_names(data, course):
    """Function that selects names and rates of students
    with the same courses and sorts them by rates

    :param data: list of dicts
    :param course: set of strings
    :return: list of tuples
    """

    return sorted([(item['name'], item['rate']) for item in data if item['course'] == course], key=lambda x: x[1], reverse=True)


def get_students_table(course):
    """Function that returns representinting of table of student sorted by rates

    :param course: string
    :return: string
    """

    return 'COURSE {}\n'.format(course) + \
           '\n'.join('{:10} \t {:4} '.format(*name)
                     for name in get_names(get_data(), course)) + '\n'


if __name__ == "__main__":
    print('\n'.join(get_students_table(course) for course in get_courses(get_data())))
