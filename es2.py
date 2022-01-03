import random
a =str(input('Diga o nome do primeiro aluno!'))
b =str(input('Diga o nome do segundo aluno!'))
c =str(input('Diga o nome do terceiro aluno!'))
d =str(input('Diga o nome do quarto aluno!'))
lista = [a,b,c,d]
random.shuffle(lista)
print("O sorteado foi {}".format(lista))
