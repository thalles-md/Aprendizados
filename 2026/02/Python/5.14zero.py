contador = 0 
while True:
    n = int(input("Digite um número, ou 0 para parar: "))
    contador += 1
    if n == 0:
        contador -= 1
        print(f"Você falou {contador} números antes do 0")
        break
    
