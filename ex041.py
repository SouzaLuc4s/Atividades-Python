a = int(input('Digite um valor!'))
b = int(input('Digite um valor!'))
c = int(input('Digite mais um valor!'))
menor = a
if b < a and b < c:
    menor = b
    print('{} foi o menor digitado!'.format(menor))
if c < a and c < b:
    menor = c
    print('{} foi o menor número digitado!'.format(menor))
maior = a
if b > a and b > c:
    maior = b
    print('{} foi o menor número digitado!'.format(maior))
if c > a and c > b:
    maior = c
    print('{} foi o menor número digitado!'.format(maior))
