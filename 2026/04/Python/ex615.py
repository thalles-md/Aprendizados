lugares_vagos = [10, 2, 1, 3, 0]
ingressos_vendidos = [0, 0, 0, 0, 0]

# Tá, não é difícil.
# Eu só preciso que o número de itens da lista seja o número do input,
# E que cada item seja um dos inputs.

while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim.")
        break

    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida.")

    elif lugares_vagos[sala -1] == 0:
        print("Desculpe, sala lotada!")

    else:
        lugares = int(input(f"Quantos lugares você deseja? Há ({lugares_vagos[sala - 1]}) disponíveis: ")) 
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido.")
        else: 
            lugares_vagos[sala -1] -= lugares
            ingressos_vendidos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")
        print("Utilização das salas")

        for sala, vagos in enumerate(lugares_vagos):
            print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")


        
total_ingressos = 0
print(f"Total de Ingressos vendidos por sala: ")
for sala, ingressos in enumerate(ingressos_vendidos):
    print(f"{ingressos} vendidos na sala {sala + 1}")
    total_ingressos += ingressos
print(f"Total de Ingressos vendidos: {total_ingressos}")
