import math
ângulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {:.2f}º tem o SENO de {:.2f}º.'.format(ângulo, seno))
coseno = math.cos(math.radians(ângulo))
print('O ângulo de {:.2f}º tem o COSSENO de {:.2f}º'.format(ângulo, coseno))
tangente = math.tan(math.radians(ângulo))
print('O angulo de {:.2f}º tem a TANGENTE de {:.2f}º'.format(ângulo, tangente))
# Nesse caso precisamos usar duas fórmulas na mesma linha para primeiro transforar graus em radianos
# Assim usamos a fórmula, sin - seno, cos - cosseno, tan - tangente e radians - radianos