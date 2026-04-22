#L = [5, 9, 13]
#x = 0 
#for e in L:
#    print(f"[{x}] {e}")
#    x += 1

L = ["String", "Nome", 13]
for x, e in enumerate(L): # o primeiro valor no enumerate é por si sóo índice, então não há necessidade de criar variável.
    print(f"[{x}] {e}")

