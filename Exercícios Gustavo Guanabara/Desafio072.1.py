a = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
while True:
    n = int(input('digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
print(f'Você digitou o número {a[n]}')
resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
while resposta in 'SN':
    if resposta == 'N':
        break
    if resposta == 'S':
        n = int(input('digite um número entre 0 e 20: '))
        print(f'Você digitou o número {a[n]}')
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('Volte sempre!')