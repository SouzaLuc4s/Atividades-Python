import random
r = random.randint(0,1)
n = input('Qual número você acha que eu pensei?')
if n == r:
    print('Você acertou!!!')
else:
    print('Errouuu (voz do faustão)!')
print(r)