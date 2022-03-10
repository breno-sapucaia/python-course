n1 = 10
n2 = 3

divisao = n1 / n2
print('{0:.2f}'.format(divisao))

n3 = 1

print(f'{n3:0>10}')

print(f'{1150:0>10}')

print(f'{1150:0>10.2f}')

nome = 'Luiz Otávio'

print(f'{nome:#^50}')

nome_formatado = '{:@>14}'.format(nome)
nome_formatado = '{n}'.format(n=nome)


print(nome_formatado)
