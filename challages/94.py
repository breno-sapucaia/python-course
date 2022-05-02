cnpj = "04.252.011/0001-10"

dig1_validador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
dig2_validador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")

listaPrimeiro = [int(x) for x in list(cnpj[:12])]
print(listaPrimeiro)
print(dig1_validador)

digito1 = 11 - sum([x * y for x, y in zip(listaPrimeiro, dig1_validador)]) % 11
if digito1 > 9:
    digito1 = 0

listaPrimeiro.append(digito1)

digito2 = 11 - sum([x * y for x, y in zip(listaPrimeiro, dig2_validador)]) % 11
if digito2 > 9:
    digito2 = 0

listaPrimeiro.append(digito2)

if cnpj == "".join(str(x) for x in listaPrimeiro):
    print("CNPJ válido")
else:
    print("CNPJ inválido")
