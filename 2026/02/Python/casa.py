# Valor da Casa
# Valor do Salário
# Número de Anos 
# Se, parecela (Valor do Aluguel / Num Parcelas ao Ano) 
# > 30%, não.

casa = int(input("Qual o valor da casa?: "))
sal = int(input("Qual o seu salário mensal?: "))
anos = int(input("Em quantos anos você irá pagar?: "))
parcela = casa / (anos * 12)
if parcela <= sal * 0.3:
    print("Ótimo! Você poderá comprar a casa")
    print(f"As prestações serão de R${parcela:.2f} mensais")
elif parcela > sal * 0.3:
    print("Você não poderá comprar a casa! Pois a parcela supera 30% do seu salário mensal.")
    print(f"Seu salário mensal: R${sal}")
    print(f"30% Dele: {(sal * 0.3):.2f}")
    print(f"Valor da parcela: R${parcela:.2f}")
else: 
    print("Para essa situação eu não programei.")

