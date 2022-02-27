from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input(('Qual é a sua jogada? ')))
computador = randint (0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
if computador == 0:
    jogada = 'PEDRA'
elif computador == 1:
    jogada = 'PAPEL'
elif computador == 2:
    jogada = 'TESOURA'
print('-=' * 20)
print('Computador jogou {}'.format(jogada))
if jogador == 0:
    jogada = 'PEDRA'
elif jogador == 1:
    jogada = 'PAPEL'
elif jogador == 2:
    jogada == 'TESOURA'
else:
    jogada == 'ai... uma jaula!'
    print('Digita um número válido nessa chibata, sabe ler não?')
    print('Jogador jogou {}'.format(jogada))
print('-=' * 20)
if jogador == computador:
    print('Ficou no empate... tenta de novo para desempatar isso!!!')
elif jogador == 0 and computador == 1:
    print('COMPUTADOR VENCEU...BUÁ BUÁ BUÁ')
elif jogador == 0 and computador == 2:
    print('JOGADOR VENCEU!!!')
elif jogador == 0 and computador == 1:
    print('COMPUTADOR VENCEU...BUÁ BUÁ BUÁ')
elif jogador == 1 and computador == 0:
    print('JOGADOR VENCEU, VOCÊ É MESMO O BICHÃO HEIN!!!')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR VENCEU!!!')
elif jogador == 2 and computador == 0:
    print('COMPUTADOR VENCEU!!!')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCEU!!!')
else:
    print('')

