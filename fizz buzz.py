from random import randint


def f(n):
    if n % 5 == 0 and n % 3 == 0:
        return print(f'Fizz Buzz {n} é divisivél por 3 e 5')
    if n % 3 == 0:
        return print(f'Fizz {n} é divisivel por 3')
    if n % 5 == 0:
        return print(f'Buzz {n} é divisivél por 5')
    return n

for i in range(100):
    rand = randint(0, 100)
    print(f(rand))