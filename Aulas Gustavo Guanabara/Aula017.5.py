valores = list() #ou simplesmente colchetes vazios []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} o valor {v}')