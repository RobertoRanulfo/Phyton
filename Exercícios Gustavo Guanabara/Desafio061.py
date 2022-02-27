print('Gerador de PA')
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 0
termo = 0
termo = primeiro
while cont < 10:
    print('{} - '.format(termo),end=' ')
    termo = termo + razão
    cont = cont + 1
print('Fim')


