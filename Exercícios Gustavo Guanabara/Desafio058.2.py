from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual o seu palpite? '))
computador = randint(0,10)
contpalpite = 0
while palpite != computador:
   if palpite > computador:
       palpite = int(input('Menos, tente de novo: '))
       contpalpite += 1
   if palpite < computador:
       palpite = int(input('Mais, vamos... tente de novo: '))
       contpalpite += 1
print('Você escolheu {} e o computador escolheu {}, você ganhou em {} palpites!'.format(palpite, computador, contpalpite))