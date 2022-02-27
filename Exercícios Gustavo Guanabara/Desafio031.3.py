d = float(input('Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {:.2f}km'.format(d))
preço = d * 0.50 if d<=200 else d * 0.45
print('O preço da sua passagem será R$ {:.2f}'.format(preço))
# if simplificado