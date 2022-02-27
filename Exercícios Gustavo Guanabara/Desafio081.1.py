números = list()
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    else:
        print('Esse valor já foi digitado ')
    if resposta == 'N':
        break
print(f'Você digitou {len(números)} elementos!')
números.sort(reverse=True)
print(f'Os valores em ordem decrescente são {números}')
if 5 in números:
    print(f'O valor 5 foi encontrado na lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
