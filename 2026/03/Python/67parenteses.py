# Verificar se todos os parenteses estão fechados

# Pelo que eu tentei entender, basicamente eu vou ter que
# Para cada '(' eu empilho (append) e para cada ')' eu tiro (pop)


roda = True
while roda:
    fila = []
    pergunta = str(input("Digite seus parenteses: "))
    for p in pergunta:
        if p == "(":
             fila.append("(")
        elif p == ")" and fila:
            fila.pop()
            if not fila:
              print("Fila Vazia!!") 
        else:
            print("Isso não está certo! Mande apenas parenteses.")
            roda = False
    # Aqui
