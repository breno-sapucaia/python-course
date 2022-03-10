"""
    Listas em Python
    fatiamento
    append, isnert, pop, del, clea, extend, +
    min, max
    range
"""

texto = 'valor'
#         0    1    2    3    4    5    6    7    8    9
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#        -

print(lista[0])

string = "Braizl is s s s  the country of soccer"

l1 = string.split(' ')
for valor in string.split(' '):
    print(f'{valor} aparece {l1.count(valor)}x vezes')
