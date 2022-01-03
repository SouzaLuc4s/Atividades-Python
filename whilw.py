from random import shuffle
Nome = input('Digite seu nome! ')
data = input('Digite sua data de nascimento')
lista1 =list(range(0,100))
shuffle(lista1)
print('O cpf será {}\n Titular:{} \n Data de nascimento {} '.format(lista1,Nome,data))
