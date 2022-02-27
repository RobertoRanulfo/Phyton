n = int(input('Digite um número para calcular o seu fatorial: '))
c = n  # c é um contador de termos que começará com o n que onde começa o fatorial
f = 1
print('Calculando {}! = '.format(n),end=' ')
while c > 0:
    print('{}'.format(c),end=' ')
    print(' x ' if c > 1 else '=',end=' ')
    f = f * c #ou f *=c
    c -= 1  # ou c = c-1 ou c -= 1
print('{}'.format(f))
#print('O fatoria de {} é {}.'.format(n, f))
