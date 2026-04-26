T = [-10, -8, 0, 1, 2, 5, -2, -4]
# A menor
# A maior
# A média

# ----
# Eu imagino que: 
# Eu preciso percorrer cada uma das temperaturas com um "for temperaturas em T" e provavelmente vou precisar, ou seria uma forma de fazer, de três elses. Mas sinto que há uma maneira mais limpa. 

menor = T[0]
maior = T[0]
media = 0

for temp in T:
    media += temp
    if temp > maior:
        maior = temp
    elif temp < menor:
        menor = temp
    
media = media / len(T)
print(f"A menor temperatura é: {menor}°")
print(f"A maior temperatura é: {maior}°")
print(f"A média entre as temperaturas é: {media}")
