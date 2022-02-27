print('-' * 40)
print('LOJA SUPER BARATÃO')
print('-' * 40)
soma = 0
soma1000 = 0
cont = 0
barato = 0
produtobarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preço
    cont += 1
    if cont == 1:
        barato = preço
        produtobarato = produto
    if preço < barato:
        barato = preço
        produtobarato = produto
    if preço > 1000:
        soma1000 += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A soma de todos os produtos deu R$ {soma:.2f}')
print(f'Temos {soma1000} produtos custando mais de 1000 reais')
print(f'O produto mais barato é {produtobarato} e custa {barato}')