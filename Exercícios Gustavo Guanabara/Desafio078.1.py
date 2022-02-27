números = []
maior = 0
menor = 0
for c in range(0, 5):
    números.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = números[c]
    else:
        if números[c] > maior:
            maior = números[c]
        if números[c] < menor:
            menor = números[c]
print('-=' * 30)
print(f'Você digitou os valoes {números}')
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for i, v in enumerate(números):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(números):
    if v == menor:
        print(f'{i}...',end='')