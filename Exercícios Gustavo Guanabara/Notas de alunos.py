import math
n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))
média = 7
if (n1+n2)/2 >= média:
    print('Parabéns, você passou, sua média foi {:.2f}!!'.format((n1+n2)/2))
else:
    print('Sorry! Você não passou sua média foi {:.2f}, tente novamente próximo ano '.format((n1+n2)/2))