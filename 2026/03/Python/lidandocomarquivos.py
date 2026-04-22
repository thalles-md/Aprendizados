with open("teste.txt", "w") as texto:
    texto.write("Imagine Tólstoi escrevendo todo o livro dele assim!\n")

with open("teste.txt", "a") as texto:
#    texto.append("Seria trabalhoso!") acabei de descobrir que não existe a função append. Aparentemente eu só posso trabalhar com as funções que estão imbutidas nos objetivos de string. Mas mesmo que eu coloque write, como o modo é "a" (append) vai adicionar no final.
   texto.write("Seria trabalhoso!")

print("Concluído! Arquivo escrito.")
