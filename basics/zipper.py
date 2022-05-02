from itertools import zip_longest

cidades = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo"]

estados = ["SP", "MG", "BA"]

cidades_estados = zip_longest(estados, cidades, fillvalue="Estados")

for cidade, estados in cidades_estados:
    print(cidade, estados, sep=" - ")

print(dict(cidades_estados))
