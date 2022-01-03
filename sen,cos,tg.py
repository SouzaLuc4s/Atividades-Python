import math
n = float(input('Digite um ângulo!'))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tg = math.tan(math.radians(n))
print('O seno de {:.1f} é {:.2f}!\nO cos {:.2f}!\nE tg {:.2f}!'.format(n,sen,cos,tg))
