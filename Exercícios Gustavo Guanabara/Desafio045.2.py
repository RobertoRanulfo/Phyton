from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'tesoura')# por causa das aspas entende que cada pavra é uma string
computador = randint(0, 2)
# ele puxou a variáve itens e em colchetes pediu qual a string
# a posiçãp da string vai ser a escolha do computador
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POO!!')
sleep(0.5)
print('=-' * 20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))  # ERRO AQUI
print('=-' * 20)
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Opção inválida!!!')
else:
    if computador == 0:
        if jogador == 0:
            print('Deu empate!!')
        elif jogador == 1:
            print('Jogador venceu!!')
        elif jogador == 2:
            print('Computador venceu!!')
        else:
            print('Jogada inválida...')
    elif computador == 1:
        if jogador == 0:
            print('Computador venceu!!')
        elif jogador == 1:
            print('Deu empate!!')
        elif jogador == 2:
            print('Jogador venceu!!')
        else:
            print('Jogada inválida...')
    elif computador == 2:
        if jogador == 0:
            print('Jogador venceu!!')
        elif jogador == 1:
            print('Computador venceu!!')
        elif jogador == 2:
            print('Deu empate')
        else:
            print('Jogada inválida...')
