a = 0 
x = int(input("Em qual número deve parar? "))
if x > 0:
    while a <= x:
     print(a)
     a = a + 1 
else:
    while a >= x:
        print(a)
        a = a - 1
