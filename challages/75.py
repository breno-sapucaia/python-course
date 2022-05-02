"""
Considerando duas listas de inteiros ou floats (lista a e lista B)
Some os valores nas listas renornando uuma nova lista com os valores somados.

se uma list afor amior q a outra, a soma só vai ser considerada o tamanho da menor.
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

soma = [x + v for x, v in zip(lista_a, lista_b)]
print(soma)
