import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))
# a fórmula hypot traz a hipotenusa apenas com as informações dos catetos