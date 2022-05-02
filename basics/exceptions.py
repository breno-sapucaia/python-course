try:
    print(a)
except NameError as erro:
    print("Erro:", erro)
except Exception as erro:
    print("Ocorreu um erro inesperado:", erro)
else:
    print("Executou com sucesso!")
finally:
    print("Finalmente")
