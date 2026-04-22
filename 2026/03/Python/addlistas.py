# "Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras"

# Digite a primeira lista
# Digita a segunda lista
# Tome a terceira (junção das outras)

L1 = []
L2 = []

# Esse aqui depois de muito bater cabeça decidi ir estudar como leitura do exercício respondido

while True: 
    e = int(input("Digite o número para a primeira lista (0 para sair): "))
    if e == 0:
        break
    L1.append(e)
while True:
    # A mesma coisa do outro código
    e = int(input("Digite o número para a segunda lista (0 para sair): "))
    if e == 0:
        break
    L2.append(e)
L3 = L2[:]
L3.extend(L2)

# Na resposta tinha um "x < len da terceira, mas não vejo o motivo para isso."
print(L3)