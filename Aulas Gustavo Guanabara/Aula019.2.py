pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k in pessoas.keys():
    print(k)
print('=-'* 15)
for k in pessoas.values():
    print(k)
print('=-'* 15)
for k, v in pessoas.items():
    print(f'{k} = {v}')