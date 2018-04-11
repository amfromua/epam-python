a = int(input('Enter a '))
b = int(input('Enter b '))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
else:
    print('Result is {}'.format(a))