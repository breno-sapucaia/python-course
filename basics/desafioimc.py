import math


name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
height = float(input("Digite sua altura: "))
weight = float(input("Digite seu peso: "))
imc = weight / (height * height)
print(name, 'tem', age, 'anos e seu IMC é', math.ceil(imc))
