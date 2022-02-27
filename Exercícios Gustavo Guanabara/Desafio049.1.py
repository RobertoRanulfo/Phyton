n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} * {} = {}'.format(n, c, n * c))

# a varíavel n vai variar apenas no que o usuário digitar e vai se repetir, enquanto
# a variável c vai caminhando de 1 a 10 essa é a jogada
