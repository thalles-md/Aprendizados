cod1 = 0.5
cod2 = 1.0
cod3 = 4.0
cod5 = 7.0
cod9 = 8.0
total = 0
while True:
    inputs = float(input("Qual o código da compra? "))
    if inputs == 1:
        total = total + cod1
    elif inputs == 2:
        total = total + cod2
    elif inputs == 3:
        total = total + cod3
    elif inputs == 5:
        total = total + cod5
    elif inputs == 9:
        total = total + cod9
    elif inputs == 0:
        print(f"O seu valor total em compras foi de R${total:.2f}.") 
        break
    else:
        print("Código inválido!")

