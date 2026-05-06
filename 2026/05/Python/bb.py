estoque = {"tomate": [1000, 2.30], #Não é certo falar "igual" para esse ':' então como se diz?
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0 
print("Vendas:\n")
for operacao in venda:
    produto, quantidade = operacao #1
    preco = estoque[produto][1] #2
    custo = preco * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f}")
    estoque[produto][0] -= quantidade # 3
    total += custo
print(f"Custo total: {total:21.2f}\n")
