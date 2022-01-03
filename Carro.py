A = float(input("Quantos dias foi alugado?"))
km = float(input("Quantos km foram percorridos?"))
S = (km*0.15)+(A*60)
print("O valor a pagar é R${:.2f}!".format(S))