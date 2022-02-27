números = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)
print(números)
números[0].sort()
print(f'Os números pares digitados são {números[0]}')
números[1].sort()
print(f'Os números ímpares digitados são {números[1]}')
