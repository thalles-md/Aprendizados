# Mostrar apenas os múltiplos de 3 
# Até o número máximo escolhido

end = int(input("Último número: "))
x = 3
while x <= end:
    if x % 3 == 0:
        print(x)
        x = x + 3
    else: 
       x = x + 1

