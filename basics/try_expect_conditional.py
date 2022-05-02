def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numer = converte_numero(input("Enter a number: "))
    if numer is not None:
        print("You entered:", numer)
    else:
        print("You did not enter a number")
