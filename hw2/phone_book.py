def menu():
    """This function shows menu
    and then requests choose function
    that selects an option
    """
    print('-------------------')
    print('1\tAdd contact')
    print('2\tShow contact')
    print('3\tRemove contact')
    print('4\tExit ')
    print('___________________')
    choose(1)


def choose(n, func=0):
    """This function requests a correct_input function
    that returns a valid input value
    and this value directs to next choosen function

    :param n: value to choose a case
    :param func: value to call a specific function
    :return: to exit
    """
    option = correct_input(n)
    if option == 1:
        add()
    elif option == 2:
        show()
    elif option == 3:
        remove()
    elif option == 4:
        return
    elif option == 'yes':
        func()
    elif option == 'no':
        menu()


def correct_input(case):
    """This function is to correct an input

    :param case: 1 for menu, 2 for others functions
    :return: valid input option
    """
    if case == 1:
        number_is_not_ok = True
        # the numbers 1 to 4 range from 49 to 51 unicode table
        option = input('Choose an option ')
        while number_is_not_ok:
            option = option.replace(' ', '')
            if len(option) == 1:
                if 49 <= ord(option) <= 52:
                    number_is_not_ok = False
                    return int(option)
            else:
                option = input('Choose a valid option ')
    elif case == 2:
        wrong_string = True
        option = input('Type \'yes\' to repeat and \'no\' to go menu ')
        while wrong_string:
            option = option.replace(' ', '').lower()
            if option == 'yes' or option == 'no':
                wrong_string = False
                return option
            else:
                option = input('Choose a valid option ')


def add():
    """This function is to add
    a new contact to the phone book
    """

    name = input('Enter a contact name ')
    phone = input('Enter a phone number ')
    phone_book.append([name, phone])
    choose(2, add)


def show():
    """This function shows
    contacts with their phone numbers
    """
    count = 0
    name = input('Enter a name ')
    flag = True
    for i in range(len(phone_book)):
        if phone_book[i][0] == name:
            while flag:
                print('имя', end='')
                spaces = show_spaces(name, 1)
                print('номер')
                flag = False
            print(phone_book[i][0], end='')
            spaces = show_spaces(name, 2)
            print(phone_book[i][1])
            count += 1
    if count == 0:
        print('There is no contact with {name} name'.format(name=name))
    choose(2, show)


def show_spaces(name, case):
    """This function calculates a number
    of whitespaces that needed to
    print phone book beautifully

    :param name: name of contact
    :param case: 1 for first line with name-number, 2 for others lines
    """
    n = 0
    m = 0
    if len(name) > 3:
        n = len(name) - 3 + 5
        m = 5
    else:
        n = 5
        m = n + 3 - len(name)
    if case == 1:
        for i in range(n):
            print(' ', end='')
    elif case == 2:
        for i in range(m):
            print(' ', end='')


def remove():
    """This function removes contacts
    with the specified name
    or tells that there is no such contact
    """
    name = input('Enter a name of contact you want to delete ')
    c = 0
    i = 0
    limit = len(phone_book)
    while i < limit:
        if phone_book[i][0] == name:
            del phone_book[i]
            limit -= 1
            c += 1
        else:
            i += 1
    if c == 0:
        print('There is no contact with {name} name'.format(name=name))
    choose(2, remove)


phone_book = []
menu()
