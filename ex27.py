nome = str(input('Digite seu texto!').strip())
n = nome.upper()
n1 = n.count('A')
print('A letra A aparece {} vezes em seu texto!\n'
'A letra A aparece pela primeira vez ná posição {}!'
'\nA letra a aparece na posição {}'.format(n1,n.find('A')+1,n.rfind('A')))