import math


name = 'Breno'
age = '21'
height = 1.80
weight = 95
imc = weight / (height * height)
print(name, 'tem', age, 'anos e seu IMC é', math.ceil(imc))


'''-------------------------------------------------'''

print(f'{name} tem {age} anos e seu IMC é {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(name, age, imc))
print('{n} tem {a} anos de idade e seu imc é {i:.2f}'.format(
    n=name, a=age, i=imc))
