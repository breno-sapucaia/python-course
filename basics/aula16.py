def divisao(n1):
    def d2(n2):
        return n1 / n2
    return d2


print(divisao(10)(2))
