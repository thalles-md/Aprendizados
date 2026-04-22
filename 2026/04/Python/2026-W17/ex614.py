lugares_vagos = [10, 2, 1, 3, 0] # Aqui já tem as salas, implícitas.
ingressos_vendidos = [0, 0, 0, 0, 0]
# Há 5 Salas. E cada um dos itens de "lugares_vagos" seria uma sala e o valor de assentos disponíveis.abs

while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim.")
        break

    if sala > len(lugares_vagos) or sala < 1: ## Se a sala (escolhida) for algo além das 5 (maior que 5) ou menor que 1, inválido.
        print("Sala inválida.")

    elif lugares_vagos[sala -1] == 0: # Como por exemplo, a sala 5. Ou outras salas após o usuário comprar todos os assentos disponíveis.
        print("Desculpe, sala lotada!")

    else: # Na situação de quê tudo ocorreu bem.
        lugares = int(input(f"Quantos lugares você deseja? Há ({lugares_vagos[sala - 1]}) disponíveis: ")) # Cada índice de lugares vagos é a quantidade de lugares vagos em alguma sala (índice da lista lugares vagos)
        if lugares > lugares_vagos[sala - 1]: # Se o tanto que o user quer é maior do quê tem.
            print("Esse número de lugares não está disponível.")
        elif lugares < 0: # Se o usuário tentar comprar um número negativo de assentos.
            print("Número inválido.")
        else: 
            lugares_vagos[sala -1] -= lugares # Caso tudo ocorra bem, diminuir o tanto de lugares disponíveis após a compra de x lugares.
            ingressos_vendidos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")
        print("Utilização das salas")

        for sala, vagos in enumerate(lugares_vagos): # sala = indíce | vagos = valor da lista, agora (provavelmente) diminuido pelo usuário.
            print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)") # Sala + 1 pelo índice não ser intuitivo. Vagos, pela própria sintaxe do enumarate (x, y | Onde y é o valor do iterável) é o item de "lugares_vagos"


        
total_ingressos = 0
print(f"Total de Ingressos vendidos por sala: ")
for sala, ingressos in enumerate(ingressos_vendidos):
    print(f"{ingressos} vendidos na sala {sala + 1}")
    total_ingressos += ingressos
print(f"Total de Ingressos vendidos: {total_ingressos}")

# Ok, o quê eu quero? 
# Mostrar a quantidade de ingressos vendidos.
#  1. Uma lista do mesmo tamanho da quantidade de salas
#  2. Elementos da lista para contar quantos ingressos foram vendidos.
#  3. Printar as vendas TOTAIS

# -----
# Calma, eu tô fazendo aqui e tentando aprender com a ajuda do Claude e DeepSeek, e é bom pois o Claude fica me retrucando, tal qual Sócrates. Mas eu me pergunto como o programa vai saber, dependendo de onde eu colocar mais código, que eu estou e vendi os ingressos em tal sala específica.