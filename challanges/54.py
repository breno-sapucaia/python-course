def saudation(name):
    print(f'Hello {name}')


def _sum(*args):
    print(sum(args))


_sum(1, 2, 3)


def percent(n1, n2):
    return n1 + n1 * n2/100 if n2 != 0 else print('percentual não pode ser zero')


print(percent(100, 10))


def fizzBuzz(n1):
    if n1 % 2 == 0:
        return 'Fizz'
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'FizzBuzz'
    if n1 % 5 == 0:
        return 'Buzz'
    return n1


print(fizzBuzz(25))
