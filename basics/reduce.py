from dados import lista
from functools import reduce

acumula = 0
for item in lista:
    acumula += item

soma_lista = reduce(lambda x, y: x + y, lista)

print(soma_lista)
