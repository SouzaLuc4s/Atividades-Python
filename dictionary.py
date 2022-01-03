# -*- coding: utf-8 -*-

clientes= {
    'clientes1':{
        'Nome': 'Lucas',
        'sobrenome': 'Jesus Soares',
    },
    'clientes2' : {
        'nome': 'Gabriel',
        'sobrenome': 'Lemos Champ',
    },
    
}
for clientes_k, clientes_v in clientes.items():
  print(f'Exibindo {clientes_k}, {clientes_v}')
  for dados_k, dados_v in clientes_v.items():
    print(f'\t{dados_k} = {dados_v}')
