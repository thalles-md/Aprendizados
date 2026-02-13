# Criar um programa que pergunte dois números 
# E a operação que deve ser efetuada
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
qual = input("Qual operação deseja efetuar? (*, /, + ou -)?: ")
if qual == "*":
    valor = a * b
    print(f"O resultado é {valor}!")
elif qual == "/":
    valor = a / b
    print(f"O resultado é {valor}!")
elif qual == "+":
    valor = a + b
    print(f"O resultado é {valor}!")
elif qual == "-":
    valor = a - b
    print(f"O resultado é {valor}!")
else:
        print("Operação inválida! Escolha entre ('*', '/', '+' ou '-'")
