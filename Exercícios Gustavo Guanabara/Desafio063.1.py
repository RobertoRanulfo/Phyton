print('-'* 25)
print('Sequência de Fibonacci')
print('-'* 25)
n = int(input('Quantos termos você quer mostrar? '))
cont = 0
n1 = 0
n2 = 1
n4 = n3 + n2
print('{} -> {}'.format(n1, n2),end=' -> ')
while cont < n:
    n3 = n1 + n2
    cont +=1
    print('{}'.format(n3),end=' -> ')
    n1 = n2
    n2 = n3
print('Fim')


