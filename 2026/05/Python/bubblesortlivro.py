# Exemplo do Livro | Página 179

#L = [3, 3, 1, 5, 4]
L = [7, 4, 3, 12, 8, 5, 1, 100, 2, 3, 8, 88]

fim = len(L) #1
while fim > 1: #2
    trocou = False #3
    x = 0 #4
    while x < (fim -1): #5
        if L[x] > L[x + 1]: #6
            trocou = True #7
            temp = L[x] #8
            L[x] = L[x + 1] 
            L[x + 1] = temp
        x += 1
    if not trocou: #9
        break
    fim -= 1 #10
for e in L:
    print(e)

# 6.16 - O que acontece quando a lista já está ordenada?
# No '#5' ele vê que o x atual não é maior que o próximo,
# logo ele não executa troca. No '#9' ele vê que não houve troca e saí do loop
# do while.

# 6.17 - O quê acontece quando dois valores são iguais?
# Ele simplesmente pula. Maior não é igual.

# 6.18
