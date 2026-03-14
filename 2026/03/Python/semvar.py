# "Modifique o primeiro exemplo de forma a realizar a mesma tarefa, mas sem utilizar a variável "achou". Dica: observar a condição de saído do *while*

# O exemplo é esse:
# L = [15, 7, 27, 39]
# p = int(input("Digite o valor a procurar: "))
# achou = False
# x = 0 | Isso aqui é só um contador
# while x < len(L)
#   if L[x] == p:
#       achou = True
#       break
#   x +=1
# if achou:
#   print(f""{p} achado na posição {x}")
# else:
#   print(f"{p} não encontrado")

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0 
while x < len(L):
    if L[x] == p:
        break
    x += 1
if True:
    print(f"{p} achado na posição {x + 1}")
else:
    print(f"{p} não encontrado")