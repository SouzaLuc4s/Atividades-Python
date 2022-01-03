from time import sleep
n = int(input('Digite qual quer número!'))
n2 = n % 2
print('-=-'*20)
print('Carregando...')
print('-=-'*20)
sleep(2)
if n2 ==1:
    print('Esse número é impar!')
else:
    print('Esse número é par!')

