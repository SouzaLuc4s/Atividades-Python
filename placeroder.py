while True:
    input()
    num_1 = input('Digite um número! ')
    num_2 = input('Digite outro número! ')
    operador= input('Digite um operador! ')
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Isso deve ser um número!' )
        continue

        num_2 = int(num_2)

        num_1 = int(num_1)
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1/num_2)
    else:
        print('Operador invalido!')