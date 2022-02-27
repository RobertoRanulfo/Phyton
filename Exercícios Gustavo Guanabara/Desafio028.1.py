from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5, tente adivinhar')
jogador = int(input('Pensei no número '))
print('Processando...')
sleep(5)
if computador == jogador:
    print('Parabéns você ganhou!!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}'.format(computador, jogador))
