carrinho = []

carrinho.append(("Produto 1", 30))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 50))

print(carrinho)

preco = 0

preco = sum([x[1] for x in carrinho])
print(preco)
