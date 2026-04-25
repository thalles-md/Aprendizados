# Problema 1002 do BeeCrowd.


'''
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
Entrada

A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
Saída

    Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
'''

# Eu não entendi como colocar um número para ser double em PYTHON...
# Mas não vou desistir, e não quero usar IA para algo tão simples (tô evitando em qualquer caso)
# Vamos ver...

π = 3.14159
raio = float(input())
area = π * (raio ** 2)
print("A=",area)

# No site devmedia, encontrei um artigo que fala que em certas situações podemos usar "Decimal"
# Não é o caso. Não imagino que eu possa importar nada.
