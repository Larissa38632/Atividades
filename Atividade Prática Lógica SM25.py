estoque = [20, 15, 10, 30, 5]

def venda(estoque, indice, quantidade):
    estoque[indice] -= quantidade

def adicionar(estoque, indice, quantidade):
    estoque[indice] += quantidade

venda(estoque, 0, 3)
venda(estoque, 3, 2)
adicionar(estoque, 4, 10)

print("Estoque atualizado:")
print("Produto 1:", estoque[0])
print("Produto 2:", estoque[1])
print("Produto 3:", estoque[2])
print("Produto 4:", estoque[3])
print("Produto 5:", estoque[4])
 
