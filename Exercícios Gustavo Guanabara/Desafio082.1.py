pares = list()
ímpares = list()
n = 0
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
números = pares + ímpares
print('-=' * 30)
print(f'A lista completa é {números}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
