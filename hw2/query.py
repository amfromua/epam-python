#!/usr/bin/env python3.6


def field_filter(field_name: str, values: list):
    """ Method that adds list of string values to dictionary
    element with a given field name as a key

    :param field_name: name of field name the data will be sorted by
    :type field_name: string
    :param values: list of strings or other possible values
    :type values: list
    :return: None
    """

    filter_dict[field_name] = values


def select(*field_name: str):
    """ Method thad extends global select_list list with
    fields of keys that will be used in final function

    :param field_name: collection of field names
    :type names: collection of strings
    :return: None
    """

    select_list.extend(field_name)


def query(friends: list, *args):
    """Filtres list of friends
    
    :param friends: list of dicts
    :param args: anything
    :return: filtered list of dicts
    """

    final_list = []

    for friend in friends:
        for key, value in filter_dict.items():
            if key not in friend.keys() or friend.get(key) not in value:
                break
        else:
            final_dict = {field: friend[field] for field in select_list}
            final_list.append(final_dict)

    return final_list


if __name__ == "__main__":
    select_list = []
    filter_dict = {}
    friends = [
        {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
        {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
        {'name': 'Кто-то еще', 'gender': 'Женский', 'sport': 'Баскетбол', 'email': 'email12@email1.com'}
    ]



    result = query(
        friends,
        select('name', 'gender'),
        field_filter('sport', ['Баскетбол', 'Волейбол']),
        field_filter('gender', ['Женский'])
    )

    print(result)  # [{'name': 'Эмили', 'gender': 'Женский'}, {'name': 'Кто-то еще', 'gender': 'Женский'}]
