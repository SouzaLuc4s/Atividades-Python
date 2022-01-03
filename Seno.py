import math
n = float(input('Digite um cateto oposto!'))
n2 = float(input('Digite cateto adjacente!'))
hip = math.hypot(n,n2)
print('A hipotenusa de {} e {} é: {:.2f}!'.format(n,n2,hip))