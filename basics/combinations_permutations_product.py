from itertools import combinations, permutations, product
from math import perm

pessoa = ["Luiz", "Maria", "João", "Pedro", "Paulo"]

for grupo in combinations(pessoa, 2):
    print(grupo)

print("#" * 20)

for grupo in permutations(pessoa, 5):
    print(grupo)

product("#" * 20)

for grupo in product(pessoa, repeat=5):
    print(grupo)
