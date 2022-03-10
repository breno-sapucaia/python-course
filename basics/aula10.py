n1 = input('digte um núermo: ')
n2 = input('digite outro número: ')

if(n1.isdigit() and n2.isdigit()):
    print(int(n1) + int(n2))
else:
    print('Não é um número')


try:
    num1 = float(n1)
    num2 = float(n2)

    print(num1 + num2)
except:
    print('deu ruim')
