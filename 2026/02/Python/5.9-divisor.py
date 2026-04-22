divisor = int(input("Qual o primeiro número?: "))
dividendo = int(input("Qual o segundo número?: "))
resultado = divisor
quociente = 0

while resultado > 0:
    resultado = resultado - dividendo
    quociente += 1
print(f"O resultado de {divisor}/{dividendo} é {quociente} e o resto é {resultado}")


# Calma, calma, calma.
# O quê eu fiz sem muito cuidado no da multiplicação, terei que fazer em dobro aqui.
# O quê é a divisão? subtrações consecutivas. 
# Eu posso dividir 10 por 2 subtraindo 5 vezes.
# Mas qual é a lógica de "poder diminuir até tal quantidade"? Chegar em zero?

# Recomeçando:
# Estrutura da divisão a/b = q + r-> q.b + r
# Exemplo: 10/2 = 5 pois é possível subtrair '2' 5 vezes antes de virar negativo. (-2 -2 -2 -2 -2)
# Então eu preciso de um while que pare quando meu "a" se torne zero.
