"""
* Criar variáveis para nome (str), idade (int)
* altura (float) e peso (float) de uma pesssoa
* Criar variável com o ano atual
* obter o ano de nasciment  da pessoa
* obter o imc da pessoa com 2 casas decimais 
* exibir um texto com todos os valores na tela
"""


from datetime import date


name = input("Digite seu nome: ")
age = 21
height = 1.80
weight = 95
year = date.today().year
birth = year - age
imc = weight / (height * height)

print(f'{name} tem {age} anos e seu IMC é {imc: .2f}, sua data de nascimento é {birth}')
