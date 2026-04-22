L = [1, 7, 2, 4]
máximo = L[0]
for e in L:
    print(f"e: {e}")
    print(f"máximo: {máximo}")
    # Adicionei essa parte pois não estava entendendo muito bem como funcionava esse caminho do 'e' até o 'máximo' sem o for imprimir os outros ou ignorar possíveis números maiores na frente. Agora consigo entender bem melhor o quê se passa.
    if e > máximo:
        máximo = e
print(máximo)
