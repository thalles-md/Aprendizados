# Vou repetir esse programa aqui, pois não entendi muito bem o quê ele faz.
lugares_vagos = [10, 2, 1, 3, 0] # Cada índice é uma sala.
while True:
    sala = int(input("Sala (0 sai):"))
    if sala == 0:
        print("Fim.")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida.")
    elif lugares_vagos[sala -1] == 0:
        print("Desculpe, sala lotada!")
    # Atrás daqui contém apenas erros.
    # A partir daqui, é o quê acontece caso o usuário digite uma sala válida.
    else:
        lugares = int(input(f"Quantos lugares você deseja? Há ({lugares_vagos[sala - 1]}) disponíveis.")) # Sala é o input do user, só para eu lembrar.
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0: 
            print("Número inválido.")
        else: 
            lugares_vagos[sala -1] -= lugares
            print(f"{lugares} lugares vendidos")
        print("Utilização das salas")
        for sala, vagos in enumerate(lugares_vagos):
            print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
        # Tá aí. 
