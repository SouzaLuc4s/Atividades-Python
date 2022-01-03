s = float(input('Digite seu salário!'))
s1 = s + (s *15/100)
s2 = s + (s *10/100)
if s<=1250:
    print('Seu no salário é R${:.2f}'.format(s1))
else:
    print('Seu novo salário é R${:.2f}'.format(s2))
