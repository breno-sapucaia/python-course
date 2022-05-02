from itertools import groupby

alunos = [
    {"nome": "João", "nota": "A"},
    {"nome": "Maria", "nota": "B"},
    {"nome": "Pedro", "nota": "A"},
    {"nome": "Karla", "nota": "B"},
    {"nome": "José", "nota": "A"},
    {"nome": "Leticia", "nota": "C"},
    {"nome": "Breno", "nota": "D"},
    {"nome": "Rose", "nota": "E"},
    {"nome": "Roberto", "nota": "D"},
    {"nome": "Joana", "nota": "E"},
    {"nome": "Anderson", "nota": "C"},
]

orderByNota = lambda aluno: aluno["nota"]

alunos.sort(key=orderByNota)

alunos_agrupados = groupby(alunos, key=orderByNota)

for nota, alunos in alunos_agrupados:
    lista_alunos = list(alunos)
    print(nota, ", ".join([aluno["nome"] for aluno in lista_alunos]), len(lista_alunos), sep=" - ")
