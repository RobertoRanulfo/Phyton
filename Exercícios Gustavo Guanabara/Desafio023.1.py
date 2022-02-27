número = int(input('Digite um número: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('Analisando o número {}'.format(número))
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhares: {}'.format(m))
# um número de 0 a 9999
# bem confuso não foi usado nada de string, apenas cálculos matemáticos