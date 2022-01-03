idade = input('Digite sua idade!')
if not idade .isnumeric():
    print('Digite apenas números!')
else:
    idade = int(idade)
    maior= (idade >= 18)
    msg= 'Pode acessar!' if (maior) else 'Você deve ser maior!'
    print(msg)