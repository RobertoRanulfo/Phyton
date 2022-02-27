cont = 0
soma = 0
sn = 'S'
maior = 0
menor = 0
while sn != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma/cont
print('Você digitou {} números e a média foi {}.'.format(cont, média))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))



