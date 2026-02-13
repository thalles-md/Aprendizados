n = int(input("Digite o número para ver sua tabuada: "))
come = int(input("Digite o primeiro número para multiplicação: "))
fi = int(input("Digite o último número para multiplicação: "))
print(f"TABUADA DO {n}, de {come} até {fi}:")
while come <= fi:
    print(n * come)
    come = come + 1

