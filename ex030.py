carro = float(input('Qual a velocidade do carro?'))
m = (carro - 80)*7
if carro <=80:
    print('Estava na velocidade correta!')
else:
    print('O valor da multa foi R${}'.format(m))
