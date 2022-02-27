d = float(input('Qual a distância da viagem? '))
if d <=200:
    print('Você está prestes a começar uma viagem de {:.2f}km. O preço da sua passagem será de R$ {:.2f} '.format(d, d * 0.50))
else:
    print('Você está prestes a começar uma viagem de {:.2f}km. O preço da sua passagem será de R$ {:.2f})'.format(d, d * 0.45))



