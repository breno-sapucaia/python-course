cpf = '503.386.992-13'

arrayOfNumbers = cpf.split('.')

cpfSplited = ''.join(arrayOfNumbers).split('-')
numbers = cpfSplited[0]
digit = cpfSplited[1]

arr = list(numbers)


def get_digit(arr, m):
    return 11 - sum((abs(i) * int(v)) for i, v in enumerate(arr, -m)) % 11


is_zero = get_digit(arr, 10) > 9 and digit[0] == '0'
valid = is_zero or digit[0] == str(get_digit(arr, 10))
arr.append(get_digit(arr, 10))
valid2 = digit[1] == str(get_digit(arr, 11))

print(get_digit(arr, 11))
print('é valido' if valid and valid2 else 'não é valido')
