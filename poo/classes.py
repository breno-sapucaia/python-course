from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def idade(self):
        return self.ano_atual - self.idade

    def falar(self):
        print(self.nome)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


print(Pessoa.gera_id())


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        return self.preco - (self.preco * (porcentagem / 100))


p1 = Produto("Notebook", 2999.99)
p1.desconto(10)
print(p1.preco)

p2 = Produto("Notebook", 2999.99)
p2.desconto(20)
print(p2.preco)
