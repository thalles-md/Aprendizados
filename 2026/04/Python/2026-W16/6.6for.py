L = [] 
while True:
    #for l in L:
    #     if l == 0:
    #         break
    #     L.append(l)
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    L.append(n)
if len(L) != 0:
    for l in L:
       #  print(L[n])
       print(l)
else:
    print("Você não digitou nenhum número antes do zero!")


