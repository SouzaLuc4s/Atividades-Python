n = float(input('Digite a distancia da sua viagem!'))
d = 0.50*n
d2 = 0.45*n
if n<=200:
    print("Sua viagem custará R${:.2f}!".format(d))
else:
    print("Sua viagem custará R${:.2f}".format(d2))
