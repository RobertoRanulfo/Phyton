print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Digite o cumprimento da primeira reta: '))
r2 = float(input('Digite o cumprimneto da segunda reta: '))
r3 = float(input('Digite o cumprimneto da terceira reta: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('As retas que medem {}, {} e {} podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('As retas que medem {}, {} e {} não pode formar um triângulo.'.format(r1, r2, r3))



# para formar um triângulo cada segmento precisa ser menor que a soma do cumrpimento dos outros dois
# ou seja r1 precisar ser menor que r2+r3, r2 precisa ser menor que r1+r2 e r3 precisa ser menor que r1+r2