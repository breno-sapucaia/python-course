from dados import produtos, lista, pessoas


def aumenta_preco(p):
    p["preco"] = round(p["preco"] * 1.05, 2)
    return p


precos = map(aumenta_preco, produtos)

for produto in precos:
    print(produto)
