from dados import lista, pessoas, produtos

nova_lista = filter(lambda x: x > 5, lista)

lista_comp = [x for x in lista if x > 5]


for item in lista_comp:
    print(item)
