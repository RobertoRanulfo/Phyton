estado = dict()
brasil= list()
for c in range(0,3):
    estado['sigla'] = str(input('Unidade federativa: '))
    estado['uf'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}!')
