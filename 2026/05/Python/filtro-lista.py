lista = ["a", "a", "b", "a", "b", "b", "a"]
listaa = []
listab = []
for item in lista:
    if item == "a":
        listaa.append(item)
    else: 
        listab.append(item)

print(f"Lista A = {listaa}")
print(f"Lista B = {listab}")

