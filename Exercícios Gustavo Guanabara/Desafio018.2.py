from math import sin, cos, tan, radians
ângulo = float(input('Digite um ângulo '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo {:.2f}º tem SENO igual a {:.2f}º, COSSENO igual a {:.2f}º e TANGENTE igual a {:.2f}º'.format(ângulo, seno, cosseno, tangente))
#Nesse caso importamos apenas as fórmulas necessárias para a resolução não a biblioteca inteira


