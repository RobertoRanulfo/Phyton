import math
num = float(input('Digite um valor '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num,math.trunc(num)))
# a fórmula trunc corta a parte não inteira do número (o que vem depois da vírgula)