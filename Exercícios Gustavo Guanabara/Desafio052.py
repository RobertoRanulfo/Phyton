tot = 0  # Não entendi!!!!
n = int(input('Digite um número: '))
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end=' ')# se ele for divisível
        tot = tot + 1 #tot =+1
    else:
        print('\033[31m',end=" ")
    print('{}'.format(c),end=' ')
print('\n\33[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
