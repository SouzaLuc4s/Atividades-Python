nome =str(input('Digite seu nome completo!'))
n1 = nome.upper()
n2 = nome.lower()
n3 = len(nome.replace(" ", ""))
n4 = nome.find(" ")
print('''Seu nome somente com letras maiusculas {}..'
'Seu nome somente com letras minusculas {}.'
'Seu nome possui {} letras.'
'O seu primeiro nome tem {} letras.'''.format(n1,n2,n3,n4))