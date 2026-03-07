valor = float(input("Digite o valor a pagar: "))
cédulas = 0
atual = 100 
apagar = (valor * 100)
while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        print(f"{cédulas} cédula(s) de R${atual}.")
        if apagar < 0.1:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cédulas = 0

