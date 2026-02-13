# Multiplicação
# Apenas com adição ou subtração.
a = int(input("Qual o primeiro número? "))
b = int(input("Qual o segundo número? "))
# Tá, vamos lá:
# O quê é a multiplicação? Apenas a soma sucessiva n vezes.
# Eu quero multiplicar `a` por `b`, ou seja, somar "a" "b" vezes.
# Ok, esse é o primeiro mais complicadinho aqui.

############################################
# contador = 0 
# resultado = 0
#
#while contador <= resultado:
#    if a > b:
#        valor = valor + b
#        contador = contador + 1
#    else:
#        valor = valor + a
#        contador = contador +1
#print(valor)
############################################

# Ok, tudo até agora foi errado, vamos lá:
# Eu quero, dado dois números "a" e "b", somar "a" com ele mesmo "b" vezes.
# Então, enquanto eu não somar (com um somador) o número "b" vezes, eu somo + 1 até 
# Até chegar em "b"

somador = 0
valor = 0
while somador <= b:
    somador = somador + 1
    valor = valor + a 
valor = valor - a 
print(valor)

# FUNCIONOU!!!!!!!!!!!! Hoje, 12/02/2026, 21:27, é a primeira vez que um código me desafiou de verdade e eu senti o prazer de conseguir superar a dificuldade.
# Coisa incrível. Agora vou reler isso que eu fiz umas 20 vezes até entendi a diferença de outras coisas que estava fazendo antes e porquê agora funciona as coisas


