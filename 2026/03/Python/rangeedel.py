# Exercício 6.4: pop sem verficar

# ListaVazia = []
# ListaVazia.pop # Não acontece NADA.

# Programa 6.7: Simulação de uma fila de banco
último = 10
fila = list(range(1, último + 1))
sair = False
while not sair:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    for letra in operação: 
        if letra == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else: 
                print("Fila vazia! Ninguém para atender.")
        elif letra == "F":
            último += 1 
            fila.append(último)
        elif letra == "S":
            sair = True
            break
        else:
            print("operação inválida!")
