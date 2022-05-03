from typing import List


cnpj = "04.252.011/0001-10"

dig1_validador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
dig2_validador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def calcDig(cnpj: List, validador):
    dig = 11 - sum([x * y for x, y in zip(cnpj, validador)]) % 11
    if dig > 9:
        dig = 0
    cnpj.append(dig)
    return cnpj


cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")

listaPrimeiro = [int(x) for x in list(cnpj[:12])]

listaPrimeiro = calcDig(cnpj=listaPrimeiro, validador=dig1_validador)
listaPrimeiro = calcDig(listaPrimeiro, dig2_validador)


if cnpj == "".join(str(x) for x in listaPrimeiro):
    print("CNPJ válido")
else:
    print("CNPJ inválido")
